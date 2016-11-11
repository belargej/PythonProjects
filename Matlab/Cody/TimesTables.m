function a = TimesTables(n)
		     % Makes a matrix that has times tables up to mxm.
  a = [1:n];
  if n>1
    for i=2:n
      x = [i:i:n*i];
      a = [a;x];
    end
  end
  display(a);
end
