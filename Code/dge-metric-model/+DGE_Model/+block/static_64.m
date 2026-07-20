function [y, T, residual, g1] = static_64(y, x, params, sparse_rowval, sparse_colval, sparse_colptr, T)
residual=NaN(1, 1);
  T(21)=1+params(202)*exp(x(155));
  residual(1)=((1+y(180)+params(429)*(x(150)+x(118)))/T(21))-(1);
if nargout > 3
    g1_v = NaN(1, 1);
g1_v(1)=1/T(21);
    g1 = sparse(sparse_rowval, sparse_colval, g1_v, 1, 1);
end
end
