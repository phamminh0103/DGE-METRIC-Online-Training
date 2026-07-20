function [y, T, residual, g1] = static_70(y, x, params, sparse_rowval, sparse_colval, sparse_colptr, T)
residual=NaN(1, 1);
  T(26)=1+params(450)*params(307)*exp(x(190));
  residual(1)=((1+y(285))/T(26))-(1);
if nargout > 3
    g1_v = NaN(1, 1);
g1_v(1)=1/T(26);
    g1 = sparse(sparse_rowval, sparse_colval, g1_v, 1, 1);
end
end
