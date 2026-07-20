function [y, T, residual, g1] = static_100(y, x, params, sparse_rowval, sparse_colval, sparse_colptr, T)
residual=NaN(2, 1);
  residual(1)=((1+y(142))/(1+y(164)*y(144)))-(1);
  T(845)=exp(x(86));
  residual(2)=(params(8)*y(144)+(1-params(8))*y(142))-(params(138)*params(469)*(1-params(8))*T(845)+params(8)*((1-x(85))*(params(136)+x(84))+params(469)*T(845)*params(138)/(y(164)+1e-12)*x(85)));
if nargout > 3
    g1_v = NaN(4, 1);
g1_v(1)=1/(1+y(164)*y(144));
g1_v(2)=1-params(8);
g1_v(3)=(-(y(164)*(1+y(142))))/((1+y(164)*y(144))*(1+y(164)*y(144)));
g1_v(4)=params(8);
    g1 = sparse(sparse_rowval, sparse_colval, g1_v, 2, 2);
end
end
