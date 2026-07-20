function [y, T, residual, g1] = static_102(y, x, params, sparse_rowval, sparse_colval, sparse_colptr, T)
residual=NaN(2, 1);
  residual(1)=((1+y(65))/(1+y(87)*y(67)))-(1);
  T(847)=exp(x(30));
  residual(2)=(params(8)*y(67)+(1-params(8))*y(65))-(params(60)*params(469)*(1-params(8))*T(847)+params(8)*((1-x(29))*(params(58)+x(28))+T(847)*params(469)*params(60)/(y(87)+1e-12)*x(29)));
if nargout > 3
    g1_v = NaN(4, 1);
g1_v(1)=1/(1+y(87)*y(67));
g1_v(2)=1-params(8);
g1_v(3)=(-(y(87)*(1+y(65))))/((1+y(87)*y(67))*(1+y(87)*y(67)));
g1_v(4)=params(8);
    g1 = sparse(sparse_rowval, sparse_colval, g1_v, 2, 2);
end
end
