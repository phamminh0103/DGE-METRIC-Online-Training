function [y, T, residual, g1] = static_99(y, x, params, sparse_rowval, sparse_colval, sparse_colptr, T)
residual=NaN(2, 1);
  residual(1)=((1+y(289))/(1+y(311)*y(291)))-(1);
  T(844)=exp(x(197));
  residual(2)=(params(8)*y(291)+(1-params(8))*y(289))-(params(291)*params(469)*(1-params(8))*T(844)+params(8)*((1-x(196))*(params(289)+x(195))+params(469)*T(844)*params(291)/(y(311)+1e-12)*x(196)));
if nargout > 3
    g1_v = NaN(4, 1);
g1_v(1)=1/(1+y(311)*y(291));
g1_v(2)=1-params(8);
g1_v(3)=(-(y(311)*(1+y(289))))/((1+y(311)*y(291))*(1+y(311)*y(291)));
g1_v(4)=params(8);
    g1 = sparse(sparse_rowval, sparse_colval, g1_v, 2, 2);
end
end
