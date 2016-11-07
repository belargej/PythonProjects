function a = CheckerMatrix(n)
		     % Taking a number n produce a square 
		     % checkerboard matrix that has dim nxn.
  x=[];
  y=[];
  for i=1:n 
    if mod(i,2)==0
      for j=1:n
	if mod(j,2)==0
	  x = [x 1];
	else
	  x = [x 0];
	end
      end
    else
      for j=1:n
	if mod(j,2)==0
	  x = [x 0];
	else
	  x = [x 1];
	end
      end
    end
    y = [y;x];
    x=[];
  end
  display(x);
  display(y);
  
end
