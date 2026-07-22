function [params, calib, check] = ToyModelSOEMC_calibrate_kappas(M_, oo_, varargin)
% Calibrate commodity-specific storage-cost kappas from open-source assumptions.
%
% NOTE:
%   This calibration fits storage/holding cost only. Commodity purchase
%   expenditure is handled separately in the model using p_E * E_D_c_import.
%   In the Dynare resource constraint, the total commodity cost is written as:
%     p_E * E_D_c_import + kappa_1_c * R_c(-1) + kappa_2_c * R_c(-1)^2
%
% PURPOSE:
%   Uses the public-source annual reserve-cost table in
%   OpenSource_4Carrier_DetailedAnalysis/four_carrier_assumptions_public_sources.csv
%   to calibrate kappa_1_c and kappa_2_c for commodities in this model.
%
% MAPPING (same logic used in prior calibration update):
%   annual_cost_model = (annual_cost_usd_m / GDP_usd_m) * Y_ss
%   annual_cost_model = kappa_1_c * R_ref_c + kappa_2_c * R_ref_c^2
%
% IDENTIFICATION CHOICE:
%   The source table provides one annual cost point per commodity, so curvature
%   is not identified. By default this function sets kappa_2_c = 0 and fits
%   kappa_1_c to match the reference point exactly.
%
% INPUTS:
%   M_   : Dynare model struct (requires param_names and params)
%   oo_  : Dynare results struct (optional; used to get Y_ss if available)
%
% NAME-VALUE OPTIONS:
%   'case'            : 'central' (default) | 'low' | 'high'
%   'assumptionsFile' : full path to CSV assumptions file
%   'GDP_USD_M'       : GDP denominator in USD million (default: 430000)
%   'Y_ss'            : override steady-state output (if empty, tries oo_ then 0.2436)
%   'verbose'         : true/false (default: true)
%
% OUTPUTS:
%   params : updated parameter vector (same length/order as M_.params)
%   calib  : struct with detailed calibration diagnostics
%   check  : 0 on success, 1 if any required row/parameter is missing
%
% EXAMPLE:
%   [params_new, calib, check] = ToyModelSOEMC_calibrate_kappas(M_, oo_, 'case', 'central');
%   if check == 0
%       M_.params = params_new;
%   end

% ----------------------------------------------------------------
% Options
% ----------------------------------------------------------------
opts = struct();
opts.case = 'central';
opts.assumptionsFile = '';
opts.GDP_USD_M = 430000;
opts.Y_ss = [];
opts.verbose = true;

if mod(numel(varargin), 2) ~= 0
    error('ToyModelSOEMC_calibrate_kappas:InvalidArgs', ...
          'Name-value arguments must come in pairs.');
end
for ii = 1:2:numel(varargin)
    name = varargin{ii};
    value = varargin{ii+1};
    if ~ischar(name) && ~isstring(name)
        error('ToyModelSOEMC_calibrate_kappas:InvalidName', 'Option names must be text.');
    end
    key = lower(char(name));
    switch key
        case 'case'
            opts.case = lower(char(value));
        case 'assumptionsfile'
            opts.assumptionsFile = char(value);
        case 'gdp_usd_m'
            opts.GDP_USD_M = value;
        case 'y_ss'
            opts.Y_ss = value;
        case 'verbose'
            opts.verbose = logical(value);
        otherwise
            error('ToyModelSOEMC_calibrate_kappas:UnknownOption', 'Unknown option: %s', char(name));
    end
end

if ~any(strcmp(opts.case, {'low', 'central', 'high'}))
    error('ToyModelSOEMC_calibrate_kappas:InvalidCase', ...
          'case must be one of: low, central, high');
end

% ----------------------------------------------------------------
% Resolve assumptions file path
% ----------------------------------------------------------------
this_folder = fileparts(mfilename('fullpath'));
if isempty(opts.assumptionsFile)
    opts.assumptionsFile = fullfile(fileparts(this_folder), ...
        'OpenSource_4Carrier_DetailedAnalysis', ...
        'four_carrier_assumptions_public_sources.csv');
end
if ~exist(opts.assumptionsFile, 'file')
    error('ToyModelSOEMC_calibrate_kappas:MissingFile', ...
          'Assumptions file not found: %s', opts.assumptionsFile);
end

% ----------------------------------------------------------------
% Determine Y_ss for USD->model-unit mapping
% ----------------------------------------------------------------
if ~isempty(opts.Y_ss)
    Y_ss = opts.Y_ss;
elseif nargin >= 2 && ~isempty(oo_) && isfield(oo_, 'steady_state') && ~isempty(oo_.steady_state)
    idxY = find(strcmp(cellstr(M_.endo_names), 'Y'), 1);
    if ~isempty(idxY)
        Y_ss = oo_.steady_state(idxY);
    else
        Y_ss = 0.2436;
    end
else
    Y_ss = 0.2436;
end

if nargin >= 2 && ~isempty(oo_) && isfield(oo_, 'steady_state') && ~isempty(oo_.steady_state)
    idxP = find(strcmp(cellstr(M_.endo_names), 'p_E'), 1);
    if ~isempty(idxP)
        pE_ss = oo_.steady_state(idxP);
    else
        pE_ss = NaN;
    end
else
    pE_ss = NaN;
end

params = M_.params;
check = 0;

% ----------------------------------------------------------------
% Read assumptions CSV and pick requested case columns
% ----------------------------------------------------------------
T = readtable(opts.assumptionsFile, 'TextType', 'string');
ann_col = [upper(opts.case(1)) opts.case(2:end) '_AnnCost_USDm'];
if ~any(strcmp(T.Properties.VariableNames, ann_col))
    error('ToyModelSOEMC_calibrate_kappas:MissingColumn', ...
          'Column %s not found in assumptions file.', ann_col);
end

% Commodity mapping between model names and assumptions table rows
map = struct([]);
map(1).comm = 'oil';
map(1).carrierMatch = 'Crude oil';
map(2).comm = 'coal';
map(2).carrierMatch = 'Imported coal';

calib = struct();
calib.case = opts.case;
calib.assumptionsFile = opts.assumptionsFile;
calib.GDP_USD_M = opts.GDP_USD_M;
calib.Y_ss = Y_ss;
calib.rows = struct([]);

for mi = 1:numel(map)
    c = map(mi).comm;

    % Locate parameter indices
    idxED = find(strcmp(cellstr(M_.param_names), ['ED_' c '_bar']), 1);
    idxK1 = find(strcmp(cellstr(M_.param_names), ['kappa_1_' c]), 1);
    idxK2 = find(strcmp(cellstr(M_.param_names), ['kappa_2_' c]), 1);

    if isempty(idxED) || isempty(idxK1) || isempty(idxK2)
        check = 1;
        warning('ToyModelSOEMC_calibrate_kappas:MissingParam', ...
            'Missing parameter(s) for commodity %s in M_.param_names.', c);
        continue;
    end

    % Find corresponding assumptions row
    is_row = contains(lower(T.Carrier), lower(map(mi).carrierMatch));
    row_idx = find(is_row, 1);
    if isempty(row_idx)
        check = 1;
        warning('ToyModelSOEMC_calibrate_kappas:MissingRow', ...
            'Could not find row for %s in assumptions file.', map(mi).carrierMatch);
        continue;
    end

    coverage_txt = T.Coverage(row_idx);
    coverage_days = parse_days(coverage_txt);
    ann_cost_usd_m = T.(ann_col)(row_idx);

    ED_c_bar = params(idxED);
    R_ref = (coverage_days / 365) * ED_c_bar;

    if R_ref <= 0
        check = 1;
        warning('ToyModelSOEMC_calibrate_kappas:InvalidRref', ...
            'Reference reserve R_ref <= 0 for commodity %s.', c);
        continue;
    end

    % Convert annual cost from USD-millions to model-output units.
    annual_cost_model = (ann_cost_usd_m / opts.GDP_USD_M) * Y_ss;

    % One-point identification: set curvature to zero and fit linear term.
    k2_c = 0;
    k1_c = annual_cost_model / R_ref;

    params(idxK1) = k1_c;
    params(idxK2) = k2_c;

    calib.rows(mi).commodity = c;
    calib.rows(mi).carrier = char(T.Carrier(row_idx));
    calib.rows(mi).coverage_days = coverage_days;
    calib.rows(mi).annual_cost_usd_m = ann_cost_usd_m;
    calib.rows(mi).ED_c_bar = ED_c_bar;
    calib.rows(mi).R_ref = R_ref;
    calib.rows(mi).annual_cost_model = annual_cost_model;
    calib.rows(mi).purchase_cost_model = pE_ss * ED_c_bar;
    calib.rows(mi).kappa_1 = k1_c;
    calib.rows(mi).kappa_2 = k2_c;
    calib.rows(mi).implied_cost_at_R_ref = k1_c * R_ref + k2_c * R_ref^2;
end

if opts.verbose
    fprintf('\n=== Kappa Calibration from Open-Source Assumptions (%s case) ===\n', upper(opts.case));
    fprintf('Assumptions file: %s\n', opts.assumptionsFile);
    fprintf('GDP (USD m): %.0f | Y_ss used: %.4f\n', opts.GDP_USD_M, Y_ss);
    for mi = 1:numel(calib.rows)
        if isempty(calib.rows(mi).commodity)
            continue;
        end
        r = calib.rows(mi);
        fprintf('  [%s] carrier="%s" | coverage=%.1f d | annual cost=%.2f USDm\n', ...
            r.commodity, r.carrier, r.coverage_days, r.annual_cost_usd_m);
        fprintf('      R_ref=%.6f | p_E*ED=%.6g | kappa_1_%s=%.6g | kappa_2_%s=%.6g\n', ...
            r.R_ref, r.purchase_cost_model, r.commodity, r.kappa_1, r.commodity, r.kappa_2);
    end
    if check == 0
        fprintf('Calibration status: OK\n\n');
    else
        fprintf('Calibration status: WARN (some rows/params missing)\n\n');
    end
end

end

function d = parse_days(txt)
% Parse strings like "30.4 days" into numeric day coverage.
if ismissing(txt)
    error('ToyModelSOEMC_calibrate_kappas:MissingCoverage', 'Coverage text is missing.');
end
s = char(txt);
tok = regexp(s, '([0-9]+\.?[0-9]*)', 'tokens', 'once');
if isempty(tok)
    error('ToyModelSOEMC_calibrate_kappas:BadCoverage', ...
          'Could not parse coverage days from text: %s', s);
end
d = str2double(tok{1});
if ~isfinite(d) || d <= 0
    error('ToyModelSOEMC_calibrate_kappas:BadCoverage', ...
          'Parsed invalid coverage value from text: %s', s);
end
end
