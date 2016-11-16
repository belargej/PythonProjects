function b=MostChange(a)

  rows=size(a,1);
  MaxRow=1;
  MaxVal=0;
  MaxValHold=0;
  for i=1:rows
    fprintf("====== on row number %i ========\n",i);
    for j=1:4
      switch j
	case 1
	  MaxVal=MaxVal+25*a(i,j);
	  fprintf("  %i quarters\n",a(i,j));
	case 2
	  MaxVal=MaxVal+5*a(i,j);
	  fprintf("  %i nickels\n",a(i,j));
	case 3
	  MaxVal=MaxVal+10*a(i,j);
	  fprintf("  %i dimes\n",a(i,j));
	case 4
	  MaxVal=MaxVal+1*a(i,j);
	  fprintf("  %i pennies\n",a(i,j));
      end
    end
    fprintf (" == For row %i MaxVal=%i\n",i,MaxVal);
    if MaxVal>MaxValHold
      MaxValHold=MaxVal;
      MaxVal=0;
      MaxRow=i;
    end
  end
  b=MaxRow;
end
