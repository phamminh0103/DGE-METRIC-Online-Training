function [y, T, residual, g1] = static_79(y, x, params, sparse_rowval, sparse_colval, sparse_colptr, T)
residual=NaN(1, 1);
  T(32)=1+params(450)*params(385)*exp(x(246));
  residual(1)=((1+y(362))/T(32))-(1);
if nargout > 3
    g1_v = NaN(1, 1);
g1_v(1)=1/T(32);
    g1 = sparse(sparse_rowval, sparse_colval, g1_v, 1, 1);
end
end
