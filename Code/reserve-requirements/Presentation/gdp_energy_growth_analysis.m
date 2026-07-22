function gdp_energy_growth_analysis()
% GDP-ENERGY-GROWTH-ANALYSIS
% MATLAB rewrite of gdp_energy_growth_analysis.py
% Creates:
%   gdp_energy_panel.csv
%   gdp_carrier_panel.csv
%   gdp_energy_growth_scatter.png
%   gdp_energy_growth_conditional_scatter.png
%   gdp_energy_growth_regression.txt
%   gdp_carrier_growth_regression.txt

clc;

% Paths
scriptDir = fileparts(mfilename('fullpath'));
eiPath = fullfile(scriptDir, 'EI-Stats-Review-All-Data.xlsx');
eiSheet = 'Primary energy cons - EJ';

carrierSheets = struct( ...
    'oil', 'Oil Consumption - EJ', ...
    'gas', 'Gas Consumption - EJ', ...
    'coal', 'Coal Consumption - EJ', ...
    'nuclear', 'Nuclear Consumption - EJ', ...
    'hydro', 'Hydro Consumption - EJ', ...
    'renewables', 'Renewables Consumption -EJ' ...
);

outPanelCsv = fullfile(scriptDir, 'gdp_energy_panel.csv');
outCarrierPanelCsv = fullfile(scriptDir, 'gdp_carrier_panel.csv');
outScatterPng = fullfile(scriptDir, 'gdp_energy_growth_scatter.png');
outCondScatterPng = fullfile(scriptDir, 'gdp_energy_growth_conditional_scatter.png');
outRegressionTxt = fullfile(scriptDir, 'gdp_energy_growth_regression.txt');
outCarrierRegressionTxt = fullfile(scriptDir, 'gdp_carrier_growth_regression.txt');

wbIndicator = 'NY.GDP.MKTP.KD';
wbDateRange = '1960:2023';
winsorPct = 1.0;

% Colors
COLOR_POINTS = [42, 120, 214] / 255;
COLOR_LINE = [227, 73, 72] / 255;
COLOR_SURFACE = [252, 252, 251] / 255;
COLOR_INK_PRIMARY = [11, 11, 11] / 255;
COLOR_INK_SECONDARY = [82, 81, 78] / 255;
COLOR_INK_MUTED = [137, 135, 129] / 255;
COLOR_GRID = [225, 224, 217] / 255;
COLOR_AXIS = [195, 194, 183] / 255;
COLOR_POS = [42, 120, 214] / 255;
COLOR_NEG = [0, 131, 0] / 255;

fprintf('Loading energy panel from %s ...\n', eiPath);
energy = load_energy_panel(eiPath, eiSheet, 'energy_ej');
if isempty(energy)
    error('No energy observations loaded. Check %s and sheet %s.', eiPath, eiSheet);
end
fprintf('  %d country-year observations, %d countries, %d-%d\n', ...
    height(energy), numel(unique(energy.iso3)), min(energy.year), max(energy.year));

fprintf('Fetching World Bank GDP data (%s) ...\n', wbIndicator);
gdp = fetch_wb_gdp(unique(energy.iso3), wbIndicator, wbDateRange);
fprintf('  %d country-year GDP observations\n', height(gdp));

fprintf('Computing growth rates and merging ...\n');
panel = build_growth_panel(energy, gdp);
fprintf('  %d country-year observations with both growth rates, %d countries, %d-%d\n', ...
    height(panel), numel(unique(panel.iso3)), min(panel.year), max(panel.year));

panel = winsorize_panel(panel, winsorPct);
writetable(panel, outPanelCsv);
fprintf('  panel written to %s\n', outPanelCsv);

nCappedGdp = sum(panel.gdp_growth_pct ~= panel.gdp_growth_pct_w);
nCappedEnergy = sum(panel.energy_growth_pct ~= panel.energy_growth_pct_w);
fprintf('Winsorizing at %.0f%%/%.0f%%: capped %d GDP growth and %d energy growth observations\n', ...
    winsorPct, 100 - winsorPct, nCappedGdp, nCappedEnergy);

fprintf('Running regressions ...\n');
reg1 = run_regression_pooled(panel);
reg2 = run_regression_fe(panel);
reg3 = run_regression_conditional(panel);
reg4 = run_regression_conditional_fe(panel);

% Save main regression summary
nNeg = sum(panel.energy_growth_pct_w < 0);
write_main_regression_summary(outRegressionTxt, panel, winsorPct, nNeg, reg1, reg2, reg3, reg4);
fprintf('  regression summary written to %s\n', outRegressionTxt);

fprintf('Drawing scatterplots ...\n');
make_scatter(panel, reg1, outScatterPng, winsorPct, ...
    COLOR_POINTS, COLOR_LINE, COLOR_SURFACE, COLOR_INK_PRIMARY, COLOR_INK_SECONDARY, COLOR_INK_MUTED, COLOR_GRID, COLOR_AXIS);
fprintf('  scatterplot written to %s\n', outScatterPng);

make_conditional_scatter(panel, reg3, outCondScatterPng, winsorPct, ...
    COLOR_POS, COLOR_NEG, COLOR_SURFACE, COLOR_INK_PRIMARY, COLOR_INK_SECONDARY, COLOR_INK_MUTED, COLOR_GRID, COLOR_AXIS);
fprintf('  conditional scatterplot written to %s\n', outCondScatterPng);

fprintf('\nPooled OLS: a 1pp increase in energy consumption growth is associated with a %.3fpp change in GDP growth\n', ...
    reg1.beta(reg1.idx.energy_growth_pct_w));
condDelta = reg3.beta(reg3.idx.interaction);
fprintf('Conditional on negative energy growth, that slope shifts by %+0.3fpp (to %.3fpp), p=%.3f\n', ...
    condDelta, reg3.beta(reg3.idx.energy_growth_pct_w) + condDelta, reg3.p(reg3.idx.interaction));

fprintf('\nBuilding per-carrier growth panels ...\n');
carrierNames = fieldnames(carrierSheets);
carrierPanels = cell(numel(carrierNames), 1);
carrierFits = cell(numel(carrierNames), 1);

for i = 1:numel(carrierNames)
    carrier = carrierNames{i};
    sheet = carrierSheets.(carrier);
    cp = build_carrier_panel(carrier, sheet, energy, panel, winsorPct, eiPath);
    carrierPanels{i} = cp;
    carrierFits{i} = run_carrier_regression(cp);
    fprintf('  %-10s %d obs, %d countries\n', carrier, height(cp), numel(unique(cp.iso3)));
end

carrierPanelAll = vertcat(carrierPanels{:});
writetable(carrierPanelAll, outCarrierPanelCsv);
fprintf('  carrier panel written to %s\n', outCarrierPanelCsv);

write_carrier_regression_summary(outCarrierRegressionTxt, carrierNames, carrierPanels, carrierFits);
fprintf('  carrier regression summary written to %s\n', outCarrierRegressionTxt);

end

function map = build_ei_map()
keys = {
    'Canada','Mexico','US', ...
    'Argentina','Brazil','Chile','Colombia', ...
    'Ecuador','Peru','Trinidad & Tobago', ...
    'Venezuela','Central America', ...
    'Austria','Belgium','Bulgaria','Croatia', ...
    'Cyprus','Czech Republic','Denmark', ...
    'Estonia','Finland','France','Germany', ...
    'Greece','Hungary','Iceland','Ireland', ...
    'Italy','Latvia','Lithuania','Luxembourg', ...
    'Netherlands','North Macedonia','Norway', ...
    'Poland','Portugal','Romania','Slovakia', ...
    'Slovenia','Spain','Sweden','Switzerland', ...
    'Turkey','Ukraine','United Kingdom', ...
    'Azerbaijan','Belarus','Kazakhstan', ...
    'Russian Federation','Turkmenistan','Uzbekistan', ...
    'Iran','Iraq','Israel','Kuwait', ...
    'Oman','Qatar','Saudi Arabia', ...
    'United Arab Emirates', ...
    'Algeria','Egypt','Morocco','South Africa', ...
    'Eastern Africa','Middle Africa','Western Africa', ...
    'Australia','Bangladesh','China', ...
    'China Hong Kong SAR','India','Indonesia', ...
    'Japan','Malaysia','New Zealand', ...
    'Pakistan','Philippines','Singapore', ...
    'South Korea','Sri Lanka','Taiwan', ...
    'Thailand','Vietnam'
};
vals = {
    'CAN','MEX','USA', ...
    'ARG','BRA','CHL','COL', ...
    'ECU','PER','TTO', ...
    'VEN','', ...
    'AUT','BEL','BGR','HRV', ...
    'CYP','CZE','DNK', ...
    'EST','FIN','FRA','DEU', ...
    'GRC','HUN','ISL','IRL', ...
    'ITA','LVA','LTU','LUX', ...
    'NLD','MKD','NOR', ...
    'POL','PRT','ROU','SVK', ...
    'SVN','ESP','SWE','CHE', ...
    'TUR','UKR','GBR', ...
    'AZE','BLR','KAZ', ...
    'RUS','TKM','UZB', ...
    'IRN','IRQ','ISR','KWT', ...
    'OMN','QAT','SAU', ...
    'ARE', ...
    'DZA','EGY','MAR','ZAF', ...
    '','','', ...
    'AUS','BGD','CHN', ...
    'HKG','IND','IDN', ...
    'JPN','MYS','NZL', ...
    'PAK','PHL','SGP', ...
    'KOR','LKA','', ...
    'THA','VNM'
};
map = containers.Map(keys, vals);
end

function panel = load_energy_panel(path, sheet, valueCol)
raw = readcell(path, 'Sheet', sheet);

% Year row at row index 3 (MATLAB 1-based)
yearRow = raw(3, :);
yearCols = [];
years = [];
prevYear = -1;

for c = 2:size(raw, 2)
    v = yearRow{c};
    if ~isnumeric(v) || isnan(v) || v <= 1900 || v >= 2100
        break;
    end
    yr = floor(v);
    if yr <= prevYear
        break;
    end
    yearCols(end + 1) = c; %#ok<AGROW>
    years(end + 1) = yr; %#ok<AGROW>
    prevYear = yr;
end

eiMap = build_ei_map();
excludeKeywords = {'Total', 'Other', 'of which'};

iso3 = {};
country = {};
year = [];
value = [];

for r = 1:size(raw, 1)
    label = raw{r, 1};
    if ~(ischar(label) || isstring(label))
        continue;
    end
    label = strtrim(string(label));

    if ~isKey(eiMap, char(label))
        continue;
    end

    isExcluded = false;
    for k = 1:numel(excludeKeywords)
        if contains(label, excludeKeywords{k})
            isExcluded = true;
            break;
        end
    end
    if isExcluded
        continue;
    end

    code = string(eiMap(char(label)));
    if code == ""
        continue;
    end

    for j = 1:numel(yearCols)
        c = yearCols(j);
        yr = years(j);
        val = raw{r, c};
        if isnumeric(val) && ~isnan(val) && val > 0
            iso3{end + 1, 1} = char(code); %#ok<AGROW>
            country{end + 1, 1} = char(label); %#ok<AGROW>
            year(end + 1, 1) = yr; %#ok<AGROW>
            value(end + 1, 1) = double(val); %#ok<AGROW>
        end
    end
end

panel = table(iso3, country, year, value, ...
    'VariableNames', {'iso3', 'country', 'year', valueCol});
panel = sortrows(panel, {'iso3', 'year'});
end

function gdp = fetch_wb_gdp(iso3Codes, indicator, dateRange)
if iscell(iso3Codes)
    iso3Codes = string(iso3Codes);
end
iso3Codes = unique(string(iso3Codes));
iso3 = {};
year = [];
gdpVal = [];

iso3Codes = sort(iso3Codes);
chunkSize = 20;
for startIdx = 1:chunkSize:numel(iso3Codes)
    endIdx = min(startIdx + chunkSize - 1, numel(iso3Codes));
    chunk = iso3Codes(startIdx:endIdx);
    codes = strjoin(chunk, ';');

    rows = fetch_wb_chunk(codes, indicator, dateRange);
    for i = 1:numel(rows)
        r = rows(i);
        if isempty(r.value)
            continue;
        end
        iso3{end + 1, 1} = char(r.countryiso3code); %#ok<AGROW>
        year(end + 1, 1) = str2double(r.date); %#ok<AGROW>
        gdpVal(end + 1, 1) = double(r.value); %#ok<AGROW>
    end
end

gdp = table(iso3, year, gdpVal, ...
    'VariableNames', {'iso3', 'year', 'gdp_constant_usd'});
gdp = sortrows(gdp, {'iso3', 'year'});
end

function rowsAll = fetch_wb_chunk(codes, indicator, dateRange)
baseUrl = sprintf('https://api.worldbank.org/v2/country/%s/indicator/%s', codes, indicator);
options = weboptions('Timeout', 180);

rowsAll = struct([]);
page = 1;
while true
    payload = [];
    success = false;
    for attempt = 1:3
        try
            url = sprintf('%s?date=%s&format=json&per_page=20000&page=%d', baseUrl, dateRange, page);
            payload = webread(url, options);
            success = true;
            break;
        catch
            if attempt == 3
                rethrow(lasterror()); %#ok<LERR>
            end
        end
    end

    if ~success || ~iscell(payload) || numel(payload) < 2
        error('Unexpected World Bank API response for country chunk: %s', codes);
    end

    meta = payload{1};
    rows = payload{2};
    if ~isempty(rows)
        if isempty(rowsAll)
            rowsAll = rows;
        else
            rowsAll = [rowsAll; rows]; %#ok<AGROW>
        end
    end

    if ~isfield(meta, 'pages') || page >= meta.pages
        break;
    end
    page = page + 1;
end
end

function panel = build_growth_panel(energy, gdp)
energy = sortrows(energy, {'iso3', 'year'});
gdp = sortrows(gdp, {'iso3', 'year'});

energy.energy_growth_pct = nan(height(energy), 1);
for i = 1:height(energy)
    if i > 1 && strcmp(energy.iso3{i}, energy.iso3{i - 1})
        prev = energy.energy_ej(i - 1);
        curr = energy.energy_ej(i);
        energy.energy_growth_pct(i) = 100 * (curr / prev - 1);
    end
end

gdp.gdp_growth_pct = nan(height(gdp), 1);
for i = 1:height(gdp)
    if i > 1 && strcmp(gdp.iso3{i}, gdp.iso3{i - 1})
        prev = gdp.gdp_constant_usd(i - 1);
        curr = gdp.gdp_constant_usd(i);
        gdp.gdp_growth_pct(i) = 100 * (curr / prev - 1);
    end
end

panel = innerjoin(energy, gdp(:, {'iso3', 'year', 'gdp_growth_pct'}), 'Keys', {'iso3', 'year'});
mask = isfinite(panel.energy_growth_pct) & isfinite(panel.gdp_growth_pct);
panel = panel(mask, :);
panel = sortrows(panel, {'iso3', 'year'});
end

function panel = winsorize_panel(panel, pct)
[gdpL, gdpU] = percentile_bounds(panel.gdp_growth_pct, pct);
[engL, engU] = percentile_bounds(panel.energy_growth_pct, pct);

panel.gdp_growth_pct_w = min(max(panel.gdp_growth_pct, gdpL), gdpU);
panel.energy_growth_pct_w = min(max(panel.energy_growth_pct, engL), engU);
end

function [lower, upper] = percentile_bounds(x, pct)
x = x(isfinite(x));
x = sort(x);
if isempty(x)
    lower = NaN;
    upper = NaN;
    return;
end
lower = percentile_linear(x, pct / 100);
upper = percentile_linear(x, 1 - pct / 100);
end

function q = percentile_linear(sortedX, p)
n = numel(sortedX);
if n == 1
    q = sortedX(1);
    return;
end
pos = 1 + (n - 1) * p;
lo = floor(pos);
hi = ceil(pos);
if lo == hi
    q = sortedX(lo);
else
    w = pos - lo;
    q = sortedX(lo) * (1 - w) + sortedX(hi) * w;
end
end

function reg = run_regression_pooled(panel)
y = panel.gdp_growth_pct_w;
x1 = panel.energy_growth_pct_w;
X = [ones(height(panel), 1), x1];
coefNames = {'Intercept', 'energy_growth_pct_w'};
idx = struct('Intercept', 1, 'energy_growth_pct_w', 2);
reg = ols_cluster(X, y, panel.iso3, coefNames, idx);
end

function reg = run_regression_fe(panel)
y = panel.gdp_growth_pct_w;
x1 = panel.energy_growth_pct_w;

Diso = make_dummies(categorical(panel.iso3));
Dyr = make_dummies(categorical(panel.year));
X = [ones(height(panel), 1), x1, Diso, Dyr];

coefNames = [{'Intercept', 'energy_growth_pct_w'}, ...
    arrayfun(@(i) sprintf('iso3_FE_%d', i), 2:(size(Diso, 2) + 1), 'UniformOutput', false), ...
    arrayfun(@(i) sprintf('year_FE_%d', i), 2:(size(Dyr, 2) + 1), 'UniformOutput', false) ...
];

idx = struct('Intercept', 1, 'energy_growth_pct_w', 2);
reg = ols_cluster(X, y, panel.iso3, coefNames, idx);
end

function reg = run_regression_conditional(panel)
y = panel.gdp_growth_pct_w;
x1 = panel.energy_growth_pct_w;
neg = double(x1 < 0);
interaction = x1 .* neg;
X = [ones(height(panel), 1), x1, neg, interaction];
coefNames = {'Intercept', 'energy_growth_pct_w', 'neg_energy', 'energy_growth_pct_w:neg_energy'};
idx = struct('Intercept', 1, 'energy_growth_pct_w', 2, 'neg_energy', 3, 'interaction', 4);
reg = ols_cluster(X, y, panel.iso3, coefNames, idx);
end

function reg = run_regression_conditional_fe(panel)
y = panel.gdp_growth_pct_w;
x1 = panel.energy_growth_pct_w;
neg = double(x1 < 0);
interaction = x1 .* neg;

Diso = make_dummies(categorical(panel.iso3));
Dyr = make_dummies(categorical(panel.year));
X = [ones(height(panel), 1), x1, neg, interaction, Diso, Dyr];

coefNames = [{'Intercept', 'energy_growth_pct_w', 'neg_energy', 'energy_growth_pct_w:neg_energy'}, ...
    arrayfun(@(i) sprintf('iso3_FE_%d', i), 2:(size(Diso, 2) + 1), 'UniformOutput', false), ...
    arrayfun(@(i) sprintf('year_FE_%d', i), 2:(size(Dyr, 2) + 1), 'UniformOutput', false) ...
];

idx = struct('Intercept', 1, 'energy_growth_pct_w', 2, 'neg_energy', 3, 'interaction', 4);
reg = ols_cluster(X, y, panel.iso3, coefNames, idx);
end

function D = make_dummies(c)
C = categories(c);
n = numel(c);
k = numel(C);
if k <= 1
    D = zeros(n, 0);
    return;
end
D = zeros(n, k - 1);
for j = 2:k
    D(:, j - 1) = double(c == C{j});
end
end

function reg = ols_cluster(X, y, groups, coefNames, idx)
mask = all(isfinite(X), 2) & isfinite(y);
X = X(mask, :);
y = y(mask);
groups = groups(mask);

n = size(X, 1);
k = size(X, 2);

beta = (X' * X) \ (X' * y);
u = y - X * beta;

XtXInv = inv(X' * X);

% One-way cluster-robust covariance (country clusters)
[~, ~, gidx] = unique(groups);
G = max(gidx);
S = zeros(k, k);
for g = 1:G
    ig = (gidx == g);
    Xg = X(ig, :);
    ug = u(ig);
    xugu = Xg' * ug;
    S = S + (xugu * xugu');
end
V = XtXInv * S * XtXInv;

% Finite-sample correction
if G > 1 && n > k
    c = (G / (G - 1)) * ((n - 1) / (n - k));
    V = c * V;
end

se = sqrt(diag(V));
tStat = beta ./ se;
if G > 1
    dof = G - 1;
else
    dof = max(n - k, 1);
end
pVal = 2 * (1 - tcdf(abs(tStat), dof));

sst = sum((y - mean(y)).^2);
ssr = sum(u.^2);
R2 = 1 - ssr / sst;

reg = struct();
reg.beta = beta;
reg.se = se;
reg.t = tStat;
reg.p = pVal;
reg.R2 = R2;
reg.n = n;
reg.k = k;
reg.coefNames = coefNames;
reg.idx = idx;
reg.V = V;
end

function write_main_regression_summary(path, panel, winsorPct, nNeg, reg1, reg2, reg3, reg4)
fid = fopen(path, 'w');
if fid < 0
    error('Cannot open %s for writing.', path);
end
cleanupObj = onCleanup(@() fclose(fid)); %#ok<NASGU>

fprintf(fid, 'Energy consumption growth vs. GDP growth -- regression analysis\n');
fprintf(fid, 'Dependent variable: GDP growth (%%, y/y)   Independent variable: energy consumption growth (%%, y/y)\n');
fprintf(fid, 'Panel: %d countries, %d-%d, N = %d   (winsorized at %.0f%%/%.0f%%; %d obs with negative energy growth)\n', ...
    numel(unique(panel.iso3)), min(panel.year), max(panel.year), height(panel), winsorPct, 100 - winsorPct, nNeg);
fprintf(fid, '%s\n\n', repmat('=', 1, 78));

fprintf(fid, '(1) Pooled OLS -- gdp_growth_pct_w ~ energy_growth_pct_w\n');
fprintf(fid, '    Standard errors clustered by country\n');
fprintf(fid, '%s\n', repmat('-', 1, 78));
write_compact_reg(fid, reg1, {'Intercept', 'energy_growth_pct_w'});
fprintf(fid, '\n');

fprintf(fid, '(2) OLS with country and year fixed effects\n');
fprintf(fid, '    gdp_growth_pct_w ~ energy_growth_pct_w + C(iso3) + C(year)\n');
fprintf(fid, '    Standard errors clustered by country (fixed-effect dummies omitted below)\n');
fprintf(fid, '%s\n', repmat('-', 1, 78));
write_compact_reg(fid, reg2, {'Intercept', 'energy_growth_pct_w'});
fprintf(fid, '\n');

fprintf(fid, '(3) Conditional (asymmetric) regression\n');
fprintf(fid, '    gdp_growth_pct_w ~ energy_growth_pct_w * neg_energy\n');
fprintf(fid, '    neg_energy = 1{energy_growth_pct_w < 0}   Standard errors clustered by country\n');
fprintf(fid, '    energy-growth slope is b[energy_growth_pct_w] when energy growth >= 0,\n');
fprintf(fid, '    and b[energy_growth_pct_w] + b[energy_growth_pct_w:neg_energy] when energy growth < 0\n');
fprintf(fid, '%s\n', repmat('-', 1, 78));
write_compact_reg(fid, reg3, {'Intercept', 'energy_growth_pct_w', 'neg_energy', 'energy_growth_pct_w:neg_energy'});
fprintf(fid, '\n');

fprintf(fid, '(4) Conditional (asymmetric) regression with country and year fixed effects\n');
fprintf(fid, '    gdp_growth_pct_w ~ energy_growth_pct_w * neg_energy + C(iso3) + C(year)\n');
fprintf(fid, '    Standard errors clustered by country (fixed-effect dummies omitted below)\n');
fprintf(fid, '%s\n', repmat('-', 1, 78));
write_compact_reg(fid, reg4, {'Intercept', 'energy_growth_pct_w', 'neg_energy', 'energy_growth_pct_w:neg_energy'});
end

function write_compact_reg(fid, reg, keepNames)
fprintf(fid, '%-34s%12s%12s%12s%12s\n', 'Variable', 'Coef', 'Std.Err', 't', 'p');
for i = 1:numel(keepNames)
    nm = keepNames{i};
    idx = find(strcmp(reg.coefNames, nm), 1);
    if isempty(idx)
        continue;
    end
    fprintf(fid, '%-34s%12.4f%12.4f%12.3f%12.3f\n', nm, reg.beta(idx), reg.se(idx), reg.t(idx), reg.p(idx));
end
fprintf(fid, '\nR-squared: %.4f   N: %d\n', reg.R2, reg.n);
end

function make_scatter(panel, reg, outPath, winsorPct, ...
    COLOR_POINTS, COLOR_LINE, COLOR_SURFACE, COLOR_INK_PRIMARY, COLOR_INK_SECONDARY, COLOR_INK_MUTED, COLOR_GRID, COLOR_AXIS)

fig = figure('Color', COLOR_SURFACE, 'Position', [100, 100, 900, 650], 'Visible', 'off');
ax = axes(fig);
set(ax, 'Color', COLOR_SURFACE);
hold(ax, 'on');

scatter(ax, panel.energy_growth_pct_w, panel.gdp_growth_pct_w, 16, ...
    'MarkerFaceColor', COLOR_POINTS, 'MarkerEdgeColor', 'none', ...
    'MarkerFaceAlpha', 0.35, 'DisplayName', 'Country-year observations');

xLine = linspace(min(panel.energy_growth_pct_w), max(panel.energy_growth_pct_w), 100)';
b0 = reg.beta(reg.idx.Intercept);
b1 = reg.beta(reg.idx.energy_growth_pct_w);
plot(ax, xLine, b0 + b1 * xLine, '-', 'LineWidth', 2, 'Color', COLOR_LINE, 'DisplayName', 'Pooled OLS fit');

r2 = reg.R2;
n = reg.n;
se = reg.se(reg.idx.energy_growth_pct_w);
text(ax, 0.02, 0.97, sprintf(['GDP growth = %.2f + %.3f x energy growth\n' ...
    '(clustered s.e. = %.3f)   R^2 = %.3f   N = %d'], b0, b1, se, r2, n), ...
    'Units', 'normalized', 'HorizontalAlignment', 'left', 'VerticalAlignment', 'top', ...
    'FontSize', 10, 'Color', COLOR_INK_SECONDARY);

yline(ax, 0, 'Color', COLOR_AXIS, 'LineWidth', 0.8);
xline(ax, 0, 'Color', COLOR_AXIS, 'LineWidth', 0.8);

xlabel(ax, 'Primary energy consumption growth (%, y/y)', 'Color', COLOR_INK_PRIMARY, 'FontSize', 11);
ylabel(ax, 'Real GDP growth (%, y/y)', 'Color', COLOR_INK_PRIMARY, 'FontSize', 11);
title(ax, sprintf(['Energy consumption growth vs. GDP growth\n' ...
    'Country panel, 1965-2023 -- Energy Institute Statistical Review x World Bank']), ...
    'Color', COLOR_INK_PRIMARY, 'FontSize', 12);

text(ax, 0.5, -0.14, sprintf(['Both series winsorized at the %.0f%% / %.0f%% percentiles ' ...
    '(caps tiny-base oil-state takeoffs and war-episode outliers, does not drop them)'], winsorPct, 100 - winsorPct), ...
    'Units', 'normalized', 'HorizontalAlignment', 'center', 'VerticalAlignment', 'top', ...
    'FontSize', 8, 'Color', COLOR_INK_MUTED);

grid(ax, 'on');
ax.GridColor = COLOR_GRID;
ax.GridAlpha = 1;
ax.XColor = COLOR_INK_MUTED;
ax.YColor = COLOR_INK_MUTED;

lg = legend(ax, 'Location', 'southeast', 'Box', 'off');
set(lg, 'TextColor', COLOR_INK_SECONDARY, 'FontSize', 9);

exportgraphics(fig, outPath, 'Resolution', 150);
close(fig);
end

function make_conditional_scatter(panel, reg, outPath, winsorPct, ...
    COLOR_POS, COLOR_NEG, COLOR_SURFACE, COLOR_INK_PRIMARY, COLOR_INK_SECONDARY, COLOR_INK_MUTED, COLOR_GRID, COLOR_AXIS)

fig = figure('Color', COLOR_SURFACE, 'Position', [100, 100, 900, 650], 'Visible', 'off');
ax = axes(fig);
set(ax, 'Color', COLOR_SURFACE);
hold(ax, 'on');

isPos = panel.energy_growth_pct_w >= 0;
isNeg = panel.energy_growth_pct_w < 0;
pos = panel(isPos, :);
neg = panel(isNeg, :);

scatter(ax, pos.energy_growth_pct_w, pos.gdp_growth_pct_w, 16, ...
    'MarkerFaceColor', COLOR_POS, 'MarkerEdgeColor', 'none', ...
    'MarkerFaceAlpha', 0.35, 'DisplayName', 'Energy growth >= 0');
scatter(ax, neg.energy_growth_pct_w, neg.gdp_growth_pct_w, 16, ...
    'MarkerFaceColor', COLOR_NEG, 'MarkerEdgeColor', 'none', ...
    'MarkerFaceAlpha', 0.35, 'DisplayName', 'Energy growth < 0');

b0 = reg.beta(reg.idx.Intercept);
b1 = reg.beta(reg.idx.energy_growth_pct_w);
d0 = reg.beta(reg.idx.neg_energy);
d1 = reg.beta(reg.idx.interaction);
pD1 = reg.p(reg.idx.interaction);

if ~isempty(pos)
    xPos = linspace(0, max(pos.energy_growth_pct_w), 50)';
    plot(ax, xPos, b0 + b1 * xPos, '-', 'LineWidth', 2.5, 'Color', COLOR_POS, ...
        'DisplayName', sprintf('Fit, energy growth >= 0 (slope %.3f)', b1));
end
if ~isempty(neg)
    xNeg = linspace(min(neg.energy_growth_pct_w), 0, 50)';
    plot(ax, xNeg, (b0 + d0) + (b1 + d1) * xNeg, '-', 'LineWidth', 2.5, 'Color', COLOR_NEG, ...
        'DisplayName', sprintf('Fit, energy growth < 0 (slope %.3f)', b1 + d1));
end

nPos = height(pos);
nNeg = height(neg);
text(ax, 0.02, 0.97, sprintf(['Slope, energy growth >= 0:  %.3f  (N = %d)\n' ...
    'Slope, energy growth < 0:  %.3f  (N = %d)\n' ...
    'Difference in slopes: %+0.3f  (p = %.3f)   R^2 = %.3f'], ...
    b1, nPos, b1 + d1, nNeg, d1, pD1, reg.R2), ...
    'Units', 'normalized', 'HorizontalAlignment', 'left', 'VerticalAlignment', 'top', ...
    'FontSize', 10, 'Color', COLOR_INK_SECONDARY);

yline(ax, 0, 'Color', COLOR_AXIS, 'LineWidth', 0.8);
xline(ax, 0, 'Color', COLOR_AXIS, 'LineWidth', 0.8);

xlabel(ax, 'Primary energy consumption growth (%, y/y)', 'Color', COLOR_INK_PRIMARY, 'FontSize', 11);
ylabel(ax, 'Real GDP growth (%, y/y)', 'Color', COLOR_INK_PRIMARY, 'FontSize', 11);
title(ax, sprintf(['GDP growth conditional on the sign of energy consumption growth\n' ...
    'Country panel, 1965-2023 -- Energy Institute Statistical Review x World Bank']), ...
    'Color', COLOR_INK_PRIMARY, 'FontSize', 12);

text(ax, 0.5, -0.14, sprintf(['Both series winsorized at the %.0f%% / %.0f%% percentiles; ' ...
    'lines from gdp_growth_pct_w ~ energy_growth_pct_w * 1{energy_growth < 0}'], winsorPct, 100 - winsorPct), ...
    'Units', 'normalized', 'HorizontalAlignment', 'center', 'VerticalAlignment', 'top', ...
    'FontSize', 8, 'Color', COLOR_INK_MUTED);

grid(ax, 'on');
ax.GridColor = COLOR_GRID;
ax.GridAlpha = 1;
ax.XColor = COLOR_INK_MUTED;
ax.YColor = COLOR_INK_MUTED;

lg = legend(ax, 'Location', 'southeast', 'Box', 'off');
set(lg, 'TextColor', COLOR_INK_SECONDARY, 'FontSize', 9);

exportgraphics(fig, outPath, 'Resolution', 150);
close(fig);
end

function panel = build_carrier_panel(carrier, sheet, totalEnergy, gdpGrowthPanel, pct, eiPath)
carrierEj = load_energy_panel(eiPath, sheet, 'carrier_ej');

combined = innerjoin(carrierEj, totalEnergy(:, {'iso3', 'year', 'energy_ej'}), ...
    'Keys', {'iso3', 'year'});
combined = sortrows(combined, {'iso3', 'year'});

combined.carrier_growth_pct = nan(height(combined), 1);
combined.share = combined.carrier_ej ./ combined.energy_ej;
combined.share_lag = nan(height(combined), 1);

for i = 1:height(combined)
    if i > 1 && strcmp(combined.iso3{i}, combined.iso3{i - 1})
        combined.carrier_growth_pct(i) = 100 * (combined.carrier_ej(i) / combined.carrier_ej(i - 1) - 1);
        combined.share_lag(i) = combined.share(i - 1);
    end
end

mask = isfinite(combined.carrier_growth_pct) & isfinite(combined.share_lag);
combined = combined(mask, :);

[cL, cU] = percentile_bounds(combined.carrier_growth_pct, pct);
combined.carrier_growth_pct_w = min(max(combined.carrier_growth_pct, cL), cU);

panel = innerjoin(combined, gdpGrowthPanel(:, {'iso3', 'year', 'gdp_growth_pct_w'}), ...
    'Keys', {'iso3', 'year'});
panel.carrier = repmat({carrier}, height(panel), 1);

panel = panel(:, {'carrier', 'iso3', 'country', 'year', 'carrier_ej', ...
    'carrier_growth_pct', 'carrier_growth_pct_w', 'share_lag', 'gdp_growth_pct_w'});
panel = sortrows(panel, {'carrier', 'iso3', 'year'});
end

function reg = run_carrier_regression(panel)
y = panel.gdp_growth_pct_w;
xg = panel.carrier_growth_pct_w;
xs = panel.share_lag;
xi = xg .* xs;
X = [ones(height(panel), 1), xg, xs, xi];
coefNames = {'Intercept', 'carrier_growth_pct_w', 'share_lag', 'carrier_growth_pct_w:share_lag'};
idx = struct('Intercept', 1, 'carrier_growth_pct_w', 2, 'share_lag', 3, 'interaction', 4);
reg = ols_cluster(X, y, panel.iso3, coefNames, idx);
end

function write_carrier_regression_summary(path, carrierNames, carrierPanels, carrierFits)
fid = fopen(path, 'w');
if fid < 0
    error('Cannot open %s for writing.', path);
end
cleanupObj = onCleanup(@() fclose(fid)); %#ok<NASGU>

fprintf(fid, 'GDP growth vs. per-carrier energy consumption growth -- regression analysis\n');
fprintf(fid, 'Dependent variable: GDP growth (%%, y/y, winsorized -- gdp_growth_pct_w)\n');
fprintf(fid, 'Independent variable: carrier''s own consumption growth (%%, y/y, winsorized\n');
fprintf(fid, 'per carrier -- carrier_growth_pct_w), interacted with share_lag = that\n');
fprintf(fid, 'carrier''s share of TOTAL primary energy consumption in the PREVIOUS year.\n');
fprintf(fid, 'The interaction tests whether a carrier''s growth matters more for GDP\n');
fprintf(fid, 'growth the larger its predetermined weight in the energy mix.\n');
fprintf(fid, '%s\n\n', repmat('=', 1, 88));

fprintf(fid, 'Summary across carriers\n');
fprintf(fid, '%s\n', repmat('-', 1, 88));
fprintf(fid, '%-12s%7s%12s%14s%16s%13s%8s\n', ...
    'Carrier', 'N', 'b(growth)', 'b(share_lag)', 'b(interaction)', 'p(interact)', 'R2');
for i = 1:numel(carrierNames)
    carrier = carrierNames{i};
    fit = carrierFits{i};
    fprintf(fid, '%-12s%7d%12.3f%14.3f%16.3f%13.3f%8.3f\n', ...
        carrier, fit.n, ...
        fit.beta(fit.idx.carrier_growth_pct_w), ...
        fit.beta(fit.idx.share_lag), ...
        fit.beta(fit.idx.interaction), ...
        fit.p(fit.idx.interaction), ...
        fit.R2);
end
fprintf(fid, '\n%s\n\n', repmat('=', 1, 88));

for i = 1:numel(carrierNames)
    carrier = carrierNames{i};
    fit = carrierFits{i};
    cp = carrierPanels{i};
    fprintf(fid, '(%d) %s -- gdp_growth_pct_w ~ carrier_growth_pct_w * share_lag\n', i, carrier);
    fprintf(fid, '    N = %d, %d countries, %d-%d\n', ...
        height(cp), numel(unique(cp.iso3)), min(cp.year), max(cp.year));
    fprintf(fid, '    Standard errors clustered by country\n');
    fprintf(fid, '%s\n', repmat('-', 1, 88));
    write_compact_reg(fid, fit, {'Intercept', 'carrier_growth_pct_w', 'share_lag', 'carrier_growth_pct_w:share_lag'});
    fprintf(fid, '\n');
end
end
