function sum = SumVect(vec)
  % This is documentation --------
  % This function takes an input vector
  % and returns the sum of all members of the vector
  
  sz = size(vec,2);
fprintf("The vector has size = %d\n",sz);
sum = 0;
for i = 1:sz
	  sum = sum+vec(i);
end
fprintf("Sum = %d\n\n",sum);

end
