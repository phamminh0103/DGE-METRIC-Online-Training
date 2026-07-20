function [y, T, residual, g1] = dynamic_98(y, x, params, steady_state, sparse_rowval, sparse_colval, sparse_colptr, T)
residual=NaN(1, 1);
  T(854)=1+x(284)*params(475)*exp(x(285))+(1-x(284))*params(474);
  residual(1)=((1+x(284)*y(477)+y(478)*(1-x(284)))/T(854))-(1);
if nargout > 3
    g1_v = NaN(1, 1);
g1_v(1)=(1-x(284))/T(854);
    g1 = sparse(sparse_rowval, sparse_colval, g1_v, 1, 1);
end
end
