function [p1,p2]=Goldbach(n)
  p1=n;
  p2=n;

  x=primes(n);
  summed=false;
  for i=1:size(x,2)
    for j=i:size(x,2)
      if x(i)+x(j)==n
	p1=x(i);
	p2=x(j);
	summed=true;
      end
      if summed==true
	break
      end
    end
    if summed==true
      break
    end
  end
end
