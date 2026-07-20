function [y, T, residual, g1] = static_128(y, x, params, sparse_rowval, sparse_colval, sparse_colptr, T)
residual=NaN(1, 1);
  residual(1)=((1+y(357))/(1+params(360)+x(241)+x(242)+x(249)*y(13)*x(248)/y(332)))-(1);
if nargout > 3
    g1_v = NaN(1, 1);
g1_v(1)=1/(1+params(360)+x(241)+x(242)+x(249)*y(13)*x(248)/y(332));
    g1 = sparse(sparse_rowval, sparse_colval, g1_v, 1, 1);
end
end
