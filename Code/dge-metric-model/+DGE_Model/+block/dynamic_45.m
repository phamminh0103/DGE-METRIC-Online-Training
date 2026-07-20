function [y, T, residual, g1] = dynamic_45(y, x, params, steady_state, sparse_rowval, sparse_colval, sparse_colptr, T)
residual=NaN(1, 1);
  T(14)=1+params(450)*params(154)*exp(x(79));
  residual(1)=((1+y(593))/T(14))-(1);
if nargout > 3
    g1_v = NaN(1, 1);
g1_v(1)=1/T(14);
    g1 = sparse(sparse_rowval, sparse_colval, g1_v, 1, 1);
end
end
