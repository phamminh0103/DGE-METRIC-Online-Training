function [y, T, residual, g1] = dynamic_75(y, x, params, steady_state, sparse_rowval, sparse_colval, sparse_colptr, T)
residual=NaN(1, 1);
  T(33)=1+params(358)*exp(x(267));
  residual(1)=((1+y(789)+params(429)*(x(262)+x(230)))/T(33))-(1);
if nargout > 3
    g1_v = NaN(1, 1);
g1_v(1)=1/T(33);
    g1 = sparse(sparse_rowval, sparse_colval, g1_v, 1, 1);
end
end
