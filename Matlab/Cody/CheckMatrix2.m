function a = CheckMatrix2(n)
				% this makes a checkerboard matrix
				% of dimension nxn, but it is smarter.
  x = ones(n);
  for i=1:n
    for j=1:n
      if mod(i,2)==0
	if mod(j,2)!=0
	  x(j,i)=0;
	end
      else
	if mod(j,2)==0
	  x(j,i)=0;
	end
      end
    end
  end
  display(x);
  
end
