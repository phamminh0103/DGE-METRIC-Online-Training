function [y, T, residual, g1] = static_95(y, x, params, sparse_rowval, sparse_colval, sparse_colptr, T)
residual=NaN(1, 1);
  residual(1)=(y(136))-(y(136)*params(26)+params(128)*(1-params(26))*(1+min(1,max(0,exp(params(25)*(y(444)-y(455)))-1))));
if nargout > 3
    g1_v = NaN(1, 1);
g1_v(1)=1-params(26);
    g1 = sparse(sparse_rowval, sparse_colval, g1_v, 1, 1);
end
end
