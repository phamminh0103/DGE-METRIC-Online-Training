function [y, T, residual, g1] = static_78(y, x, params, sparse_rowval, sparse_colval, sparse_colptr, T)
residual=NaN(1, 1);
  T(31)=1+exp(x(247));
  residual(1)=((1+y(347))/T(31))-(1);
if nargout > 3
    g1_v = NaN(1, 1);
g1_v(1)=1/T(31);
    g1 = sparse(sparse_rowval, sparse_colval, g1_v, 1, 1);
end
end
