function [y, T, residual, g1] = dynamic_123(y, x, params, steady_state, sparse_rowval, sparse_colval, sparse_colptr, T)
residual=NaN(1, 1);
  residual(1)=((1+y(658))/(1+params(204)+x(129)+x(130)+x(137)*y(468)*x(136)/y(633)))-(1);
if nargout > 3
    g1_v = NaN(1, 1);
g1_v(1)=1/(1+params(204)+x(129)+x(130)+x(137)*y(468)*x(136)/y(633));
    g1 = sparse(sparse_rowval, sparse_colval, g1_v, 1, 1);
end
end
