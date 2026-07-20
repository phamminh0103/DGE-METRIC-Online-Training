function [y, T, residual, g1] = static_46(y, x, params, sparse_rowval, sparse_colval, sparse_colptr, T)
residual=NaN(1, 1);
  T(9)=1+params(49)*exp(x(44));
  residual(1)=((1+y(33)+params(429)*(x(39)+x(7)))/T(9))-(1);
if nargout > 3
    g1_v = NaN(1, 1);
g1_v(1)=1/T(9);
    g1 = sparse(sparse_rowval, sparse_colval, g1_v, 1, 1);
end
end
