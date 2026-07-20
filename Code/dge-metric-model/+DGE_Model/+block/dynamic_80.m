function [y, T, residual, g1] = dynamic_80(y, x, params, steady_state, sparse_rowval, sparse_colval, sparse_colptr, T)
residual=NaN(1, 1);
  residual(1)=((1+y(899)+params(429)*(x(291)+x(289)+x(284)+x(293)))/(1+params(466)+x(292)+x(286)))-(1);
if nargout > 3
    g1_v = NaN(1, 1);
g1_v(1)=1/(1+params(466)+x(292)+x(286));
    g1 = sparse(sparse_rowval, sparse_colval, g1_v, 1, 1);
end
end
