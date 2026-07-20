function [y, T] = dynamic_88(y, x, params, steady_state, sparse_rowval, sparse_colval, sparse_colptr, T)
  y(591)=params(26)*y(136)+(1-params(26))*params(128)*(1+min(1,max(0,exp(params(25)*(y(444)-y(455)))-1)));
end
