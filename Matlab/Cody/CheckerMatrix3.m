function a = CheckerMatrix3(n)
  % this is the easiest way to make a checkerboard matrix
  t = mod(1:n,2);
  a = toeplitz(t,t);
  display(a);

end
