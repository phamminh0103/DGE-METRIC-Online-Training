function [y, T, residual, g1] = dynamic_60(y, x, params, steady_state, sparse_rowval, sparse_colval, sparse_colptr, T)
residual=NaN(1, 1);
  T(24)=1+exp(x(132))+(params(477)+x(122))*x(125);
  residual(1)=((1+y(632))/T(24))-(1);
if nargout > 3
    g1_v = NaN(1, 1);
g1_v(1)=1/T(24);
    g1 = sparse(sparse_rowval, sparse_colval, g1_v, 1, 1);
end
end
