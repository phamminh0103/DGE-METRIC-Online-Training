function [y, T, residual, g1] = static_134(y, x, params, sparse_rowval, sparse_colval, sparse_colptr, T)
residual=NaN(1, 1);
  residual(1)=((1+y(413))/(1+y(407)+y(413)*(1-params(428))))-(1);
if nargout > 3
    g1_v = NaN(1, 1);
g1_v(1)=(1+y(407)+y(413)*(1-params(428))-(1-params(428))*(1+y(413)))/((1+y(407)+y(413)*(1-params(428)))*(1+y(407)+y(413)*(1-params(428))));
    g1 = sparse(sparse_rowval, sparse_colval, g1_v, 1, 1);
end
end
