function order=PerfectPlacement(list)

  index=[1:size(list,1)];
  sumVal=1;
##  while sumVal!=0
    for i=1:size(list,1)
      if i+1<size(list,1)+1
	display("In if statement ----");
	sumVal=sumVal+abs(list(i,2)-list(i+1,1));
      end
      display(sumVal);
      if sumVal==0
      else
	
      end
 ## end
  

end
