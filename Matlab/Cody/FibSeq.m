function a = FibSeq(n)
			  % this function calculates the nth number in
			  % the fibonacci sequence.
  x = 1;
  y = 1;

  if n==0
    return;
  elseif n==1
    a=1;
  elseif n==2
    a=1;
  else
    for i=3:n
      a=x+y;
      x=y;
      y=a;
    end

  end
  fprintf("Fib(%i) = %i\n",n,a);
end
