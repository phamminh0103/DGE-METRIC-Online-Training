function [y, T, residual, g1] = static_55(y, x, params, sparse_rowval, sparse_colval, sparse_colptr, T)
residual=NaN(1, 1);
  T(15)=1+params(127)*exp(x(100));
  residual(1)=((1+y(110)+params(429)*(x(95)+x(63)))/T(15))-(1);
if nargout > 3
    g1_v = NaN(1, 1);
g1_v(1)=1/T(15);
    g1 = sparse(sparse_rowval, sparse_colval, g1_v, 1, 1);
end
end
