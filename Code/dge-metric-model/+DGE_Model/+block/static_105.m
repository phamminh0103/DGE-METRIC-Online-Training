function [y, T, residual, g1] = static_105(y, x, params, sparse_rowval, sparse_colval, sparse_colptr, T)
residual=NaN(1, 1);
  T(848)=1+x(284)*params(475)*exp(x(285))+(1-x(284))*params(474);
  residual(1)=((1+x(284)*y(22)+y(23)*(1-x(284)))/T(848))-(1);
if nargout > 3
    g1_v = NaN(1, 1);
g1_v(1)=(1-x(284))/T(848);
    g1 = sparse(sparse_rowval, sparse_colval, g1_v, 1, 1);
end
end
