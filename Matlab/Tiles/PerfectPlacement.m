function order=PerfectPlacement(list)
  
  index=[1:size(list,1)];
  sumVal=1;
  counter=0;
  MaxLoops=factorial(size(list,1));
  orderings=[1:size(list,1)];
  
  while sumVal!=0 || counter!=MaxLoops
    ## this sums for one particular ordering of the list.
    for i=1:size(list,1)
      if i+1<size(list,1)+1
	display("In if statement ----");
	sumVal=sumVal+abs(list(i,2)-list(i+1,1));
      end
      display(sumVal);

      ## if the sumVal==0 then you are done.
      if sumVal==0
      else ## otherwise you need to re-order the list and try again.
	goodSwap=false;
	indexComp=[1:size(list,1)];
	index=indexComp;
	while goodSwap==false
	  index(1)=index(2);
	  index(2)=indexComp(1);
	  for i=1:size(orderings,1)
	    if index==orderings(i,:)
	    else
	      break;
	    end
	end
	
      end
      counter=counter+1;
    end
    

end
