function score = OrderedDoms(list,order)
	 % Take a list of ordered pairs an the order they should be in
	 % then get the sum of the abs diff of the yeilds. For Example
	 % list = [1 2;5 3;2 4] order = [1 2 3]
	 % yeilds = [1 2][5 3][2 4] 
	 %         abs(2-5)+abs(3-2)=4

  ## In this section we reoder the list based on the input order.
  sz=size(order,2);
  originalList = list;
  for i=1:sz
    val=order(i);
    if val==i
    else
      if originalList(val,:)==list(i,:)
      else
	holder=originalList(val,:);
	list(i,:)=holder;
      end
    end
  end
  display(list);


  ## now in this section we want to do the summing.
  sum=0;
  rows=size(list,1);
  for i=1:rows
    if i+1==rows+1
    else
      sum = sum+abs(list(i,2)-list(i+1,1));
    end
  end
  display(sum);
end
