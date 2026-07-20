function [y, T, residual, g1] = dynamic_125(y, x, params, steady_state, sparse_rowval, sparse_colval, sparse_colptr, T)
residual=NaN(1, 1);
  residual(1)=((1+y(511))/(1+params(51)+x(18)+x(19)+x(26)*y(468)*x(25)/y(486)))-(1);
if nargout > 3
    g1_v = NaN(1, 1);
g1_v(1)=1/(1+params(51)+x(18)+x(19)+x(26)*y(468)*x(25)/y(486));
    g1 = sparse(sparse_rowval, sparse_colval, g1_v, 1, 1);
end
end
