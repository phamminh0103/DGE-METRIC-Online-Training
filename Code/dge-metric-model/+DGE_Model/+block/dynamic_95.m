function [y, T, residual, g1] = dynamic_95(y, x, params, steady_state, sparse_rowval, sparse_colval, sparse_colptr, T)
residual=NaN(2, 1);
  residual(1)=((1+y(744))/(1+y(766)*y(746)))-(1);
  T(853)=exp(x(197));
  residual(2)=(params(8)*y(746)+(1-params(8))*y(744))-(params(291)*params(469)*(1-params(8))*T(853)+params(8)*((1-x(196))*(params(289)+x(195))+params(469)*T(853)*params(291)/(y(766)+1e-12)*x(196)));
if nargout > 3
    g1_v = NaN(4, 1);
g1_v(1)=1/(1+y(766)*y(746));
g1_v(2)=1-params(8);
g1_v(3)=(-(y(766)*(1+y(744))))/((1+y(766)*y(746))*(1+y(766)*y(746)));
g1_v(4)=params(8);
    g1 = sparse(sparse_rowval, sparse_colval, g1_v, 2, 2);
end
end
