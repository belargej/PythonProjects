function a =StuffTheBoard(input,rows,cols)
   % Take an input vector, and a number of rows and
   % columns and return a matrix that is rowsxcols with indexes of the
   % original vector, throwing out the lowest values.

  inSize = size(input,2);
  MaxDim = rows*cols;
  index=[1:inSize];
  outMat=zeros(rows,cols);
  if inSize<MaxDim
    fprintf("   You want a matrix that is %ix%i\n",rows,cols);
    fprintf("   But you only have %i elements.\n",inSize);
    return;
  end

  lowHold=1;
  lowVal=input(1);
  tossedOut=[];
  while inSize>MaxDim
    fprintf("------- Beginning Loop ---------\n");
    fprintf(" Max Dim = %i\n",MaxDim);
    fprintf(" inSize  = %i\n",inSize);
    lowHold=1;
    lowVal=input(1);
    for i=2:inSize
      if input(i)<lowVal
	lowHold=i;
	lowVal=input(i);
      end
    end
    input(lowHold)=[];
    index(lowHold)=[];
    tossedOut = [tossedOut lowHold];
    inSize=size(input,2);
    
    fprintf(" Low Value = %i\n",lowVal);
    fprintf(" Low Place = %i\n",lowHold);
  end

  for i=1:MaxDim
    outMat(i)=index(i);
  end
  display(input);
  display(tossedOut);
  display(index);
  display(outMat);
end
