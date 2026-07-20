function [y, T, residual, g1] = dynamic_93(y, x, params, steady_state, sparse_rowval, sparse_colval, sparse_colptr, T)
residual=NaN(2, 1);
  residual(1)=((1+y(667))/(1+y(689)*y(669)))-(1);
  T(851)=exp(x(141));
  residual(2)=(params(8)*y(669)+(1-params(8))*y(667))-(params(213)*params(469)*(1-params(8))*T(851)+params(8)*((1-x(140))*(params(211)+x(139))+params(469)*T(851)*params(213)/(y(689)+1e-12)*x(140)));
if nargout > 3
    g1_v = NaN(4, 1);
g1_v(1)=(-(y(689)*(1+y(667))))/((1+y(689)*y(669))*(1+y(689)*y(669)));
g1_v(2)=params(8);
g1_v(3)=1/(1+y(689)*y(669));
g1_v(4)=1-params(8);
    g1 = sparse(sparse_rowval, sparse_colval, g1_v, 2, 2);
end
end
