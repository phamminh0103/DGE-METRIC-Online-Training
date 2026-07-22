% ToyModelSOEMC_joint_optimal.m
% Joint Optimal Policy: Reserve Stock × Drawdown Rule × Capacity Investment
%
% ECONOMIC QUESTION:
%   What combination of (phi_R, phi_IQ, d) jointly maximises expected welfare?
%
%   These three dimensions are INTERDEPENDENT and must be optimised together:
%     d      = days of reserve coverage (sets R_oil_bar, R_coal_bar)
%              More reserves = better insurance BUT higher storage cost
%              (storage cost kappa_1_c*R + kappa_2_c*R^2 is in the resource constraint
%               so it already reduces C in every simulation draw — no double counting)
%     phi_R  = drawdown intensity (how aggressively reserves are released in a crisis)
%              Only valuable if the stock is large enough to sustain drawdown
%     phi_IQ = capacity investment rate (raises Q_c_bar, making reserves more effective)
%              Strategic complement: higher Q makes each unit of reserves worth more
%
%   JOINT OPTIMUM:
%     (phi_R*, phi_IQ*, d*) = argmax_{phi_R, phi_IQ, d}  E[W(phi_R, phi_IQ, d)]
%
%   NOTE: E[W] already accounts for storage costs through the model's resource constraint:
%     Y = C + I + sum_c(IQ_c + ToT_c + kappa_1_c*R_c(-1) + kappa_2_c*R_c(-1)^2)
%   So the objective is simply maximum expected welfare — no separate cost subtraction.
%
% APPROACH: Extended-path Monte Carlo on a 3-dimensional policy grid.
%   Outer loop: d (reserve level) — changes R_c_bar, requires SS re-solve
%     Middle loop: phi_IQ        — changes Q_c_bar, requires SS re-solve
%       Inner loop: phi_R        — no SS change
%         MC draws: N_MC_joint extended_path runs
%
% OUTPUT:
%   W_joint  : (N_d × N_phi_IQ × N_phi_R) matrix of mean welfare
%   Optimal (d*, phi_IQ*, phi_R*) written to workspace and M_.params updated
%
% HOW TO USE:
%   Called from ToyModelSOEMC_run.m (Step 4).
%   Requires M_, options_, oo_ in workspace (from dynare run).

% ----------------------------------------------------------------
% COMMODITY LIST  (must match @#define COMM in ToyModelSOEMC.mod)
% ----------------------------------------------------------------
COMM   = {'oil', 'coal'};
N_COMM = length(COMM);

% ----------------------------------------------------------------
% SETTINGS
% ----------------------------------------------------------------
beta        = 0.97;     % Vietnam calibration
T_MC        = 100;      % simulation length
T_WELFARE   = T_MC;     % welfare horizon (full simulation)

if ~exist('MINIMAL_MODE', 'var')
    MINIMAL_MODE = false;
end
if ~exist('TRAINING_MODE', 'var')
    TRAINING_MODE = false;
end

if MINIMAL_MODE
    N_MC_joint = 1;      % Fastest mode: one draw per point
else
    N_MC_joint = 30;     % Full mode
end

% ANNUAL MODEL — must use 'pf' with shock_gen Bernoulli crisis events.
% EP mode with Gaussian shocks is WRONG here: small per-period sigma → expected
% drawdown >> refill rate → stock depletes to 0 → insurance value = 0 (spurious result).
SIM_MODE = 'pf';

% ----------------------------------------------------------------
% POLICY GRIDS
%   d: days of import coverage (reserve level)
%      Expressed in days so results are directly interpretable.
%      R_c_bar(d) = (d/365) * ED_c_bar_c  [model units, annual]
%
%   phi_R:  [0, 0.5, 1.0]   — no/partial/full drawdown
%   phi_IQ: [0.02, 0.04, 0.08] — baseline, moderate, high (EMP VIII) investment
%
%   NOTE: d=0 excluded from phi_R variation (no stock to release);
%         phi_IQ_grid excludes 0 to avoid Q_c_bar=0 singularity.
% ----------------------------------------------------------------
if TRAINING_MODE
    d_grid      = [30,  90];
    phi_R_grid  = [0.5, 1.0];
    phi_IQ_grid = [0.04, 0.08];
elseif MINIMAL_MODE
    d_grid      = [90];
    phi_R_grid  = [0.5];
    phi_IQ_grid = [0.08];
else
    d_grid      = [0 1:10:100];%[0, 30, 90, 180, 365];
    phi_R_grid  = [0.5, 1.0];%[0, 0.5, 1.0];
    phi_IQ_grid = [0.01, 0.02];%[0.02, 0.04, 0.08];
end

N_d      = length(d_grid);
N_phi_R  = length(phi_R_grid);
N_phi_IQ = length(phi_IQ_grid);

% ----------------------------------------------------------------
% Parameter indices
% ----------------------------------------------------------------
idx_phi_R  = find(strcmp(M_.param_names, 'phi_R'));
idx_phi_IQ = find(strcmp(M_.param_names, 'phi_IQ'));

% ED_c_bar values (annual import volumes)
ED_c_bar = struct();
for ci = 1:N_COMM
    c = COMM{ci};
    ED_c_bar.(c) = M_.params(strcmp(M_.param_names, ['ED_' c '_bar']));
end

% ----------------------------------------------------------------
% Solver options
% ----------------------------------------------------------------
options_ep            = options_;
options_ep.ep.periods   = 100;
options_ep.ep.verbosity = 0;

options_pf = options_;
options_pf.periods = T_MC;
PF_HOMOTOPY_STEPS = 5;   % Default continuation steps per PF draw

% ----------------------------------------------------------------
% Shock panels
%   Pre-generate one Monte Carlo shock panel per draw and reuse it across
%   all policy grid points so the comparison across d is on the same shocks.
% ----------------------------------------------------------------
rng_state = rng;
seed_fixed = 1;
rng(seed_fixed, 'twister');
oo_shock_base = perfect_foresight_setup(M_, options_pf, oo_);
exo_draws = cell(N_MC_joint, 1);
shock_report = struct();
shock_report.seed = seed_fixed;
shock_report.draws = cell(N_MC_joint, 1);
for kk = 1:N_MC_joint
    exo_draws{kk} = ToyModelSOEMC_shock_gen(M_, oo_shock_base, T_MC, COMM, struct());
    draw_report = struct();
    for ci = 1:N_COMM
        c = COMM{ci};
        idx_ed_ci = find(strcmp(M_.exo_names, ['e_' c '_shock']));
        draw_report.(c).e_shock = exo_draws{kk}(2:T_MC+1, idx_ed_ci);
    end
    shock_report.draws{kk} = draw_report;
end
rng(rng_state);

shock_dir = fullfile(fileparts(mfilename('fullpath')), 'run_outputs');
if ~exist(shock_dir, 'dir')
    mkdir(shock_dir);
end
shock_file = fullfile(shock_dir, 'joint_optimal_shocks.mat');
save(shock_file, 'shock_report', 'exo_draws', 'd_grid', 'phi_R_grid', 'phi_IQ_grid', 'T_MC', '-v7.3');
fprintf('  Saved shock paths for inspection: %s\n', shock_file);

% ----------------------------------------------------------------
% Storage
% ----------------------------------------------------------------
W_joint     = NaN(N_d, N_phi_IQ, N_phi_R);   % mean discounted welfare at each grid point
Cmean_joint = NaN(N_d, N_phi_IQ, N_phi_R);   % mean consumption over full simulation
n_failed    = zeros(N_d, N_phi_IQ, N_phi_R);

total_calls = N_d * N_phi_IQ * N_phi_R * N_MC_joint;
fprintf('\n=== JOINT OPTIMAL POLICY: Reserve Stock × Drawdown × Capacity ===\n\n');
fprintf('  Grid:  d = [%s] days\n', num2str(d_grid));
fprintf('         phi_R  = [%s]\n', num2str(phi_R_grid,  '%.2f '));
fprintf('         phi_IQ = [%s]\n', num2str(phi_IQ_grid, '%.2f '));
fprintf('  N_MC = %d draws per point  |  Total EP calls: %d\n\n', N_MC_joint, total_calls);
fprintf('  (Storage cost is in the resource constraint — use both E[W] and mean C.)\n\n');

progress_count = 0;
wb_start_time  = tic;
progress_bar   = [];
if usejava('desktop')
    wb_msg = sprintf('Starting — 0 / %d simulations  |  grid: %d×%d×%d', ...
                     total_calls, N_d, N_phi_IQ, N_phi_R);
    progress_bar = waitbar(0, wb_msg, ...
        'Name', 'Joint Optimal Policy  —  Monte Carlo Progress', ...
        'CreateCancelBtn', 'setappdata(gcbf,''cancel'',true)');
    setappdata(progress_bar, 'cancel', false);
end
progress_cleanup = onCleanup(@() close_progress_bar(progress_bar));

% Parallelize over reserve days grid when Parallel Computing Toolbox is available.
parallel_days = false;
if license('test', 'Distrib_Computing_Toolbox')
    try
        p = gcp('nocreate');
        if isempty(p)
            % Use process-based workers: ToyModelSOEMC_steadystate calls save,
            % which is unsupported on thread-based workers.
            p = parpool('local');
        elseif strcmp(p.Cluster.Type, 'threads')
            delete(p);
            p = parpool('local');
        end
        parallel_days = ~isempty(p);
    catch ME_pool
        fprintf('  Parallel pool unavailable; using serial loop (%s).\n', ME_pool.message);
        parallel_days = false;
    end
end
parallel_cleanup = onCleanup(@() close_parallel_pool(parallel_days));

if parallel_days
    fprintf('  Parallel mode: parfor over d-grid (%d workers).\n\n', gcp('nocreate').NumWorkers);
else
    fprintf('  Serial mode: for-loop over d-grid.\n\n');
end

% ----------------------------------------------------------------
% OUTER LOOP: d (reserve level)
%   Sets R_c_bar(d) for all commodities proportionally to import volume.
%   Re-solved in each phi_IQ iteration (SS depends on both d and phi_IQ).
% ----------------------------------------------------------------
if parallel_days
    parfor di = 1:N_d
        d = d_grid(di);
        M_loc = M_;
        oo_loc = oo_;

        for ci = 1:N_COMM
            c = COMM{ci};
            R_val = (d / 365) * ED_c_bar.(c);
            M_loc.params(strcmp(M_loc.param_names, ['R_' c '_bar'])) = R_val;
        end

        W_di = NaN(N_phi_IQ, N_phi_R);
        C_di = NaN(N_phi_IQ, N_phi_R);
        F_di = zeros(N_phi_IQ, N_phi_R);

        for ii = 1:N_phi_IQ
            phi_IQ = phi_IQ_grid(ii);

            M_loc.params(idx_phi_IQ) = phi_IQ;
            exo_ss = zeros(1, M_loc.exo_nbr);
            [ys_ij, params_ij, ~] = ToyModelSOEMC_steadystate([], exo_ss, M_loc, options_ep);
            oo_loc.steady_state = ys_ij;
            M_loc.params        = params_ij;

            if strcmp(SIM_MODE, 'pf')
                oo_pf_base = perfect_foresight_setup(M_loc, options_pf, oo_loc);
            else
                oo_pf_base = oo_loc;
            end

            for jj = 1:N_phi_R
                phi_R = phi_R_grid(jj);
                M_loc.params(idx_phi_R) = phi_R;

                W_draws = NaN(N_MC_joint, 1);
                C_draws = NaN(N_MC_joint, 1);
                n_fail_ij = 0;

                for kk = 1:N_MC_joint
                    try
                        if strcmp(SIM_MODE, 'ep')
                            oo_ep = oo_loc;
                            oo_ep = extended_path([], T_MC, options_ep, M_loc, oo_ep);
                            C_path = extract_var(oo_ep, M_loc, 'C');
                        else
                            exo_mat = exo_draws{kk};
                            [oo_run, ~] = ToyModelSOEMC_pf_homotopy_solve(M_loc, options_pf, oo_pf_base, exo_mat, PF_HOMOTOPY_STEPS);
                            C_path = extract_var(oo_run, M_loc, 'C');
                        end
                        W_draws(kk) = compute_welfare(C_path, beta, T_WELFARE);
                        C_draws(kk) = mean(C_path(:), 'omitnan');
                    catch
                        n_fail_ij = n_fail_ij + 1;
                    end
                end

                W_di(ii, jj) = mean(W_draws, 'omitnan');
                C_di(ii, jj) = mean(C_draws, 'omitnan');
                F_di(ii, jj) = n_fail_ij;
            end
        end

        W_joint(di, :, :) = W_di;
        Cmean_joint(di, :, :) = C_di;
        n_failed(di, :, :) = F_di;
    end
else
    for di = 1:N_d
        d = d_grid(di);
        R_d = struct();
        for ci = 1:N_COMM
            c = COMM{ci};
            R_d.(c) = (d / 365) * ED_c_bar.(c);
            M_.params(strcmp(M_.param_names, ['R_' c '_bar'])) = R_d.(c);
        end

        fprintf('--- d = %4d days  (R_oil=%.3f, R_coal=%.3f) ---\n', ...
                d, R_d.oil, R_d.coal);

        for ii = 1:N_phi_IQ
            phi_IQ = phi_IQ_grid(ii);

            M_.params(idx_phi_IQ) = phi_IQ;
            exo_ss = zeros(1, M_.exo_nbr);
            [ys_ij, params_ij, ~] = ToyModelSOEMC_steadystate([], exo_ss, M_, options_ep);
            oo_.steady_state = ys_ij;
            M_.params        = params_ij;

            if strcmp(SIM_MODE, 'pf')
                oo_ = perfect_foresight_setup(M_, options_pf, oo_);
            end

            C_ss_ij = ys_ij(strcmp(M_.endo_names, 'C'));
            fprintf('  phi_IQ=%.2f  C_ss=%.4f  Q_oil_bar=%.4f\n', phi_IQ, C_ss_ij, ...
                    M_.params(strcmp(M_.param_names, 'Q_oil_bar')));

            for jj = 1:N_phi_R
                phi_R = phi_R_grid(jj);
                M_.params(idx_phi_R) = phi_R;

                W_draws = NaN(N_MC_joint, 1);
                C_draws = NaN(N_MC_joint, 1);
                n_fail_ij = 0;

                if ~isempty(progress_bar) && isvalid(progress_bar)
                    wb_combo = sprintf('d=%dd  \x03D5_R=%.2f  \x03D5_{IQ}=%.2f  (%d/%d done)', ...
                        d, phi_R, phi_IQ, progress_count, total_calls);
                    waitbar(progress_count / total_calls, progress_bar, wb_combo);
                end

                for kk = 1:N_MC_joint
                    if ~isempty(progress_bar) && isvalid(progress_bar) && getappdata(progress_bar,'cancel')
                        fprintf('\n  *** Run cancelled by user at %d/%d simulations. ***\n', ...
                                progress_count, total_calls);
                        break;
                    end

                    try
                        if strcmp(SIM_MODE, 'ep')
                            extended_path([], T_MC, options_ep, M_, oo_);
                            C_path = extract_var(oo_, M_, 'C');
                        else
                            exo_mat = exo_draws{kk};
                            [oo_run, ~] = ToyModelSOEMC_pf_homotopy_solve(M_, options_pf, oo_, exo_mat, PF_HOMOTOPY_STEPS);
                            C_path = extract_var(oo_run, M_, 'C');
                        end
                        W_draws(kk) = compute_welfare(C_path, beta, T_WELFARE);
                        C_draws(kk) = mean(C_path(:), 'omitnan');
                    catch
                        n_fail_ij = n_fail_ij + 1;
                    end

                    progress_count = progress_count + 1;
                    if ~isempty(progress_bar) && isvalid(progress_bar)
                        elapsed   = toc(wb_start_time);
                        rate      = progress_count / elapsed;
                        remaining = (total_calls - progress_count) / max(rate, 1e-6);
                        if remaining > 60
                            eta_str = sprintf('%.0f min left', remaining / 60);
                        else
                            eta_str = sprintf('%.0f s left', remaining);
                        end
                        wb_msg = sprintf('d=%dd  \x03D5_R=%.2f  \x03D5_{IQ}=%.2f  | MC %d/%d  | %s', ...
                            d, phi_R, phi_IQ, kk, N_MC_joint, eta_str);
                        waitbar(progress_count / total_calls, progress_bar, wb_msg);
                    end
                end

                W_joint(di, ii, jj)  = mean(W_draws, 'omitnan');
                Cmean_joint(di, ii, jj) = mean(C_draws, 'omitnan');
                n_failed(di, ii, jj) = n_fail_ij;

                fprintf('    phi_R=%.1f  E[W]=%.4f  mean(C)=%.4f  (fail:%d/%d)\n', ...
                    phi_R, W_joint(di,ii,jj), Cmean_joint(di,ii,jj), n_fail_ij, N_MC_joint);
            end
        end
    end
end

% Restore calibration defaults
M_.params(idx_phi_R)  = 0.5;
M_.params(idx_phi_IQ) = 0.04;

% ----------------------------------------------------------------
% FIND JOINT OPTIMUM
%   Normalize the two criteria to [0,1] and combine them equally.
% ----------------------------------------------------------------
W_norm = local_scale01(W_joint);
C_norm = local_scale01(Cmean_joint);
objective_joint = 0.5 * W_norm + 0.5 * C_norm;

[objective_max, idx_best] = max(objective_joint(:));
[di_opt, ii_opt, jj_opt] = ind2sub(size(W_joint), idx_best);

d_opt      = d_grid(di_opt);
phi_IQ_opt = phi_IQ_grid(ii_opt);
phi_R_opt  = phi_R_grid(jj_opt);

EW_opt    = W_joint(di_opt, ii_opt, jj_opt);
Cmean_opt = Cmean_joint(di_opt, ii_opt, jj_opt);

R_oil_opt  = (d_opt / 365) * ED_c_bar.oil;
R_coal_opt = (d_opt / 365) * ED_c_bar.coal;

% ----------------------------------------------------------------
% WRITE OPTIMAL VALUES TO M_.params AND RE-SOLVE SS
% ----------------------------------------------------------------
M_.params(strcmp(M_.param_names, 'R_oil_bar'))  = R_oil_opt;
M_.params(strcmp(M_.param_names, 'R_coal_bar')) = R_coal_opt;
M_.params(idx_phi_IQ) = phi_IQ_opt;
M_.params(idx_phi_R)  = phi_R_opt;

[ys_opt, params_opt, ~] = ToyModelSOEMC_steadystate([], zeros(1,M_.exo_nbr), M_, options_ep);
oo_.steady_state = ys_opt;
M_.params        = params_opt;

% Unit conversion for reporting: map normalized model output to billion EUR.
Y_ss_opt  = ys_opt(strcmp(M_.endo_names, 'Y'));
GDP_BN_EUR = 500;
eur_bn_per_model_unit = GDP_BN_EUR / Y_ss_opt;
Cmean_opt_eur_bn = Cmean_opt * eur_bn_per_model_unit;

% Store optimal policy in workspace for downstream scripts
phi_R_star  = phi_R_opt;
phi_IQ_star = phi_IQ_opt;
d_star      = d_opt;

% ----------------------------------------------------------------
% CONSOLE RESULTS
% ----------------------------------------------------------------
fprintf('\n  ============================================================\n');
fprintf('  JOINT OPTIMAL POLICY (Vietnam, annual model)\n');
fprintf('  ============================================================\n');
fprintf('  Reserve stock:     d* = %d days of import coverage\n', d_opt);
fprintf('                     R_oil_bar*  = %.4f  (annual model units)\n', R_oil_opt);
fprintf('                     R_coal_bar* = %.4f  (annual model units)\n', R_coal_opt);
fprintf('  Drawdown rule:     phi_R*  = %.2f\n', phi_R_opt);
fprintf('  Capacity invest.:  phi_IQ* = %.2f\n', phi_IQ_opt);
fprintf('  Mean consumption at optimum: %.2f bn EUR\n', Cmean_opt_eur_bn);
fprintf('  composite score:    %.4f\n', objective_max);
fprintf('\n  Interpretation:\n');
fprintf('  The jointly optimal policy requires BOTH adequate reserves AND\n');
fprintf('  sufficient installed capacity. Sub-optimal on either dimension\n');
fprintf('  reduces the welfare gain from the other (strategic complementarity).\n');
fprintf('  Reserve choice uses a 50/50 blend of normalized NPV and mean consumption.\n\n');

% ----------------------------------------------------------------
% SAVE RESULTS TO ONE CSV FILE
% ----------------------------------------------------------------
C_ss_opt     = ys_opt(strcmp(M_.endo_names, 'C'));
k1_oil       = M_.params(strcmp(M_.param_names, 'kappa_1_oil'));
k2_oil       = M_.params(strcmp(M_.param_names, 'kappa_2_oil'));
k1_coal      = M_.params(strcmp(M_.param_names, 'kappa_1_coal'));
k2_coal      = M_.params(strcmp(M_.param_names, 'kappa_2_coal'));
cost_oil     = k1_oil  * R_oil_opt  + k2_oil  * R_oil_opt^2;
cost_coal    = k1_coal * R_coal_opt + k2_coal * R_coal_opt^2;
cost_pct     = (cost_oil + cost_coal) / C_ss_opt * 100;

W_zero   = W_joint(1, ii_opt, 1);     % smallest d, phi_R=0 ≈ no-reserve benchmark
C_zero   = Cmean_joint(1, ii_opt, 1);
lambda_b = (exp((EW_opt - W_zero) * (1 - beta)) - 1) * 100;

C_d_opt = squeeze(Cmean_joint(:, ii_opt, jj_opt));   % mean consumption at optimal phi_R, phi_IQ for each d
C_d_opt_eur_bn = C_d_opt * eur_bn_per_model_unit;

grid_d_days  = repelem(d_grid(:), numel(phi_R_grid) * numel(phi_IQ_grid));
grid_phi_R   = repmat(repelem(phi_R_grid(:), numel(phi_IQ_grid)), numel(d_grid), 1);
grid_phi_IQ  = repmat(phi_IQ_grid(:), numel(d_grid) * numel(phi_R_grid), 1);
grid_W_mean  = W_joint(:);
grid_C_mean  = Cmean_joint(:);
grid_score   = objective_joint(:);
grid_n_fail  = n_failed(:);
grid_n_draws = repmat(N_MC_joint, numel(grid_W_mean), 1);
grid_is_opt  = (grid_d_days == d_opt) & (grid_phi_R == phi_R_opt) & (grid_phi_IQ == phi_IQ_opt);

grid_table = table(repmat("grid", numel(grid_W_mean), 1), grid_d_days, grid_phi_R, grid_phi_IQ, ...
    grid_W_mean, grid_C_mean, grid_score, grid_n_fail, grid_n_draws, grid_is_opt, ...
    NaN(numel(grid_W_mean),1), NaN(numel(grid_W_mean),1), NaN(numel(grid_W_mean),1), NaN(numel(grid_W_mean),1), ...
    NaN(numel(grid_W_mean),1), NaN(numel(grid_W_mean),1), NaN(numel(grid_W_mean),1), NaN(numel(grid_W_mean),1), ...
    NaN(numel(grid_W_mean),1), NaN(numel(grid_W_mean),1), ...
    'VariableNames', {'row_type','d_days','phi_R','phi_IQ','W_mean','C_mean','objective_score','n_failed','n_draws','is_optimal', ...
                      'C_ss','Y_ss','R_oil_star','R_coal_star','R_oil_days','R_coal_days', ...
                      'EW_opt','EW_zero','storage_cost_pct','lambda_benefit_pct'});

curve_table = table(repmat("consumption_curve", numel(C_d_opt), 1), d_grid(:), repmat(phi_R_opt, numel(C_d_opt), 1), ...
    repmat(phi_IQ_opt, numel(C_d_opt), 1), squeeze(W_joint(:, ii_opt, jj_opt)), C_d_opt, ...
    squeeze(objective_joint(:, ii_opt, jj_opt)), NaN(numel(C_d_opt),1), NaN(numel(C_d_opt),1), false(numel(C_d_opt),1), ...
    repmat(C_ss_opt, numel(C_d_opt), 1), repmat(Y_ss_opt, numel(C_d_opt), 1), repmat(R_oil_opt, numel(C_d_opt), 1), ...
    repmat(R_coal_opt, numel(C_d_opt), 1), repmat(R_oil_opt / ED_c_bar.oil * 365, numel(C_d_opt), 1), ...
    repmat(R_coal_opt / ED_c_bar.coal * 365, numel(C_d_opt), 1), repmat(EW_opt, numel(C_d_opt), 1), ...
    repmat(W_zero, numel(C_d_opt), 1), repmat(cost_pct, numel(C_d_opt), 1), repmat(lambda_b, numel(C_d_opt), 1), ...
    'VariableNames', grid_table.Properties.VariableNames);

summary_table = table("summary", d_opt, phi_R_opt, phi_IQ_opt, EW_opt, Cmean_opt, objective_max, NaN, N_MC_joint, true, ...
    C_ss_opt, Y_ss_opt, R_oil_opt, R_coal_opt, R_oil_opt / ED_c_bar.oil * 365, R_coal_opt / ED_c_bar.coal * 365, ...
    EW_opt, W_zero, cost_pct, lambda_b, ...
    'VariableNames', grid_table.Properties.VariableNames);

results_table = [grid_table; curve_table; summary_table];
results_csv = fullfile(shock_dir, 'joint_optimal_results.csv');
writetable(results_table, results_csv);
fprintf('  Results saved to: %s\n\n', results_csv);

% ----------------------------------------------------------------
% FIGURE 1: Heatmap of E[W] at optimal d*
%   Shows phi_R × phi_IQ trade-off at the optimal reserve level.
% ----------------------------------------------------------------
figure('Name', 'Joint Optimal: Policy Heatmap at d*', 'Position', [80 80 700 520]);

W_slice = squeeze(W_joint(di_opt, :, :));   % N_phi_IQ × N_phi_R at optimal d
imagesc(phi_R_grid, phi_IQ_grid, W_slice);
colorbar;
xlabel('\phi_R  (drawdown intensity)', 'FontSize', 12);
ylabel('\phi_{IQ}  (capacity investment rate)', 'FontSize', 12);
title({sprintf('E[W] at optimal d^* = %d days of coverage', d_opt), ...
       sprintf('Optimal: \\phi_R^* = %.2f,  \\phi_{IQ}^* = %.2f', phi_R_opt, phi_IQ_opt)}, ...
      'FontWeight', 'bold', 'FontSize', 12);
set(gca, 'XTick', phi_R_grid, 'YTick', phi_IQ_grid, ...
         'XTickLabel', arrayfun(@(x) sprintf('%.2f',x), phi_R_grid, 'UniformOutput',false), ...
         'YTickLabel', arrayfun(@(x) sprintf('%.2f',x), phi_IQ_grid, 'UniformOutput',false));
hold on;
scatter(phi_R_opt, phi_IQ_opt, 250, 'g', 'filled', 'MarkerEdgeColor', 'k', ...
        'LineWidth', 2, 'DisplayName', 'Optimal (\\phi_R^*, \\phi_{IQ}^*)');
text(phi_R_opt, phi_IQ_opt, sprintf('  (%.2f, %.2f)', phi_R_opt, phi_IQ_opt), ...
     'Color', 'w', 'FontWeight', 'bold', 'FontSize', 11, 'VerticalAlignment', 'bottom');
hold off;
grid on;

% ----------------------------------------------------------------
% FIGURE 2: Mean consumption vs d at optimal (phi_R*, phi_IQ*)
%   Shows the reserve sizing dimension — how much stock matters.
% ----------------------------------------------------------------
figure('Name', 'Joint Optimal: Consumption vs Reserve Level', 'Position', [100 100 750 500]);

C_d_curve = C_d_opt_eur_bn;   % N_d vector at optimal policy, billion EUR

plot(d_grid, C_d_curve, '-o', 'Color', [0.18 0.44 0.71], 'LineWidth', 2.5, ...
     'MarkerFaceColor', [0.18 0.44 0.71], 'MarkerSize', 8);
hold on;
scatter(d_opt, Cmean_opt_eur_bn, 200, [0.13 0.60 0.33], 'filled', ...
        'MarkerEdgeColor', 'k', 'LineWidth', 1.5);
xline(d_opt, '--', 'Color', [0.13 0.60 0.33], 'LineWidth', 2, ...
      'Label', sprintf('  d^* = %d days', d_opt));
xline(90,   ':', 'Color', [0.18 0.44 0.71], 'LineWidth', 1.5, 'Label', '  IEA 90d');
xline(365,  'k--', 'LineWidth', 1, 'Label', '  1yr');
xline(730,  'k:',  'LineWidth', 1, 'Label', '  2yr');
xlim([0, 730]);
hold off;

xlabel('Days of import coverage  d', 'FontSize', 12);
ylabel('Mean consumption  E[C]  (billion EUR)', 'FontSize', 12);
title({sprintf('Mean consumption vs Reserve Level  at  \phi_R^*=%.2f, \phi_{IQ}^*=%.2f', ...
               phi_R_opt, phi_IQ_opt), ...
    sprintf('GDP anchor: Y_{ss} = %.2f maps to %.0f bn EUR', Y_ss_opt, GDP_BN_EUR)}, ...
      'FontWeight', 'bold', 'FontSize', 12);
grid on;

% ----------------------------------------------------------------
% FIGURE 3: Mean consumption vs d for all phi_R values at optimal phi_IQ*
%   Shows interaction between stock level and drawdown policy.
% ----------------------------------------------------------------
figure('Name', 'Joint Optimal: Stock-Drawdown Interaction', 'Position', [120 120 800 500]);

phi_R_colors = {[0.80 0.15 0.15], [0.18 0.44 0.71], [0.13 0.60 0.33]};
hold on; grid on;
for jj = 1:N_phi_R
    C_curve_jj = squeeze(Cmean_joint(:, ii_opt, jj)) * eur_bn_per_model_unit;
    plot(d_grid, C_curve_jj, '-o', 'Color', phi_R_colors{jj}, 'LineWidth', 2.2, ...
         'MarkerFaceColor', phi_R_colors{jj}, 'MarkerSize', 7, ...
         'DisplayName', sprintf('\\phi_R = %.2f', phi_R_grid(jj)));
end
xline(d_opt, '--', 'Color', [0.13 0.60 0.33], 'LineWidth', 2, ...
      'Label', sprintf('  d^* = %d days', d_opt));
xline(90, ':', 'Color', [0.5 0.5 0.5], 'LineWidth', 1.5, 'Label', '  IEA 90d');
scatter(d_opt, Cmean_opt_eur_bn, 200, [0.13 0.60 0.33], 'filled', ...
        'MarkerEdgeColor', 'k', 'LineWidth', 1.5, 'HandleVisibility', 'off');
hold off;

xlabel('Days of import coverage  d', 'FontSize', 12);
ylabel('Mean consumption  E[C]  (billion EUR)', 'FontSize', 12);
title({sprintf('Stock Level × Drawdown Policy  (at \\phi_{IQ}^* = %.2f)', phi_IQ_opt), ...
    sprintf('GDP anchor: Y_{ss} = %.2f maps to %.0f bn EUR', Y_ss_opt, GDP_BN_EUR)}, ...
      'FontWeight', 'bold', 'FontSize', 12);
legend('Location', 'southeast', 'FontSize', 11);

fprintf('=== Joint optimal policy analysis complete. ===\n\n');

function close_progress_bar(progress_bar)
if ~isempty(progress_bar) && isvalid(progress_bar)
    delete(progress_bar);
end
end

function close_parallel_pool(parallel_days)
if parallel_days
    p = gcp('nocreate');
    if ~isempty(p)
        delete(p);
    end
end
end

function y = local_scale01(x)
lo = min(x(:), [], 'omitnan');
hi = max(x(:), [], 'omitnan');
den = hi - lo;
if ~isfinite(den) || den <= 0
    y = zeros(size(x));
else
    y = (x - lo) ./ den;
end
end
