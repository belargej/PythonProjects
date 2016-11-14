function a=Collatz(n)
  a=[n];
  while n!=1
    if mod(n,2)==0
      n=n/2;      
    else
      n=3*n+1;
    end
    a=[a n];
    fprintf("n=%i\n",n);
  end

end
