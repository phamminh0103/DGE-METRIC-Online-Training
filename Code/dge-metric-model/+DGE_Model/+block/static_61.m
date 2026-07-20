function [y, T, residual, g1] = static_61(y, x, params, sparse_rowval, sparse_colval, sparse_colptr, T)
residual=NaN(1, 1);
  T(20)=1+params(450)*params(229)*exp(x(134));
  residual(1)=((1+y(208))/T(20))-(1);
if nargout > 3
    g1_v = NaN(1, 1);
g1_v(1)=1/T(20);
    g1 = sparse(sparse_rowval, sparse_colval, g1_v, 1, 1);
end
end
