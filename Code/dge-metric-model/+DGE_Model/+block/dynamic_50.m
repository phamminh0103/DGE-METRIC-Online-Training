function [y, T, residual, g1] = dynamic_50(y, x, params, steady_state, sparse_rowval, sparse_colval, sparse_colptr, T)
residual=NaN(1, 1);
  T(17)=1+exp(x(89));
  residual(1)=((1+y(623))/T(17))-(1);
if nargout > 3
    g1_v = NaN(1, 1);
g1_v(1)=1/T(17);
    g1 = sparse(sparse_rowval, sparse_colval, g1_v, 1, 1);
end
end
