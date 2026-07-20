function [y, T, residual, g1] = static_130(y, x, params, sparse_rowval, sparse_colval, sparse_colptr, T)
residual=NaN(1, 1);
  residual(1)=((1+y(203))/(1+params(204)+x(129)+x(130)+x(137)*y(13)*x(136)/y(178)))-(1);
if nargout > 3
    g1_v = NaN(1, 1);
g1_v(1)=1/(1+params(204)+x(129)+x(130)+x(137)*y(13)*x(136)/y(178));
    g1 = sparse(sparse_rowval, sparse_colval, g1_v, 1, 1);
end
end
