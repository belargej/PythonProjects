function out=MeanPrimes(in)
  sz=size(in,1)*size(in,2);
  sumVal=0;
  counter=0;
  for i=1:sz
    ##Check for primality.
    if primeTest(in(i))==true; ## is prime.
      counter++;
      sumVal=sumVal+in(i);      
    end
  end

  if counter>0
    out=sumVal/counter;
  else
    out=false;
  end

end


function isPrime=primeTest(n)

  prime=true;
  if mod(n,2)==0
    if n!=2
      prime=false;
    end
  elseif mod(n,3)==0
    if n!=3
      prime=false;
    end
  end

  if n==1
    prime=false;
  end
  
  if prime==true
    j=1;
    while 6*j+1<sqrt(n)
      if mod(n,6*j+1)==0
	prime=false;
      end
      j++;
    end
    k=1;
    while 6*k-1<sqrt(n)
      if mod(n,6*k-1)==0
	prime=false;
      end
      k++;
    end
  end
  isPrime=prime;
end
