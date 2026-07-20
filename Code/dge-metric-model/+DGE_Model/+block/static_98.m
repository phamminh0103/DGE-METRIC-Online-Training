function [y, T, residual, g1] = static_98(y, x, params, sparse_rowval, sparse_colval, sparse_colptr, T)
residual=NaN(2, 1);
  T(843)=exp(x(253));
  residual(1)=(params(8)*y(368)+(1-params(8))*y(366))-(params(369)*params(469)*(1-params(8))*T(843)+params(8)*((1-x(252))*(params(367)+x(251))+params(469)*T(843)*params(369)/(y(388)+1e-12)*x(252)));
  residual(2)=((1+y(366))/(1+y(388)*y(368)))-(1);
if nargout > 3
    g1_v = NaN(4, 1);
g1_v(1)=1-params(8);
g1_v(2)=1/(1+y(388)*y(368));
g1_v(3)=params(8);
g1_v(4)=(-(y(388)*(1+y(366))))/((1+y(388)*y(368))*(1+y(388)*y(368)));
    g1 = sparse(sparse_rowval, sparse_colval, g1_v, 2, 2);
end
end
