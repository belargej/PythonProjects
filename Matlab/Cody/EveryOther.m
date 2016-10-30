function eo = EveryOther(vec)
  %this selects every other element of a vector
  % and creates a new vector.
  sz = size(vec,2);
y=vec;
for i = 1:sz
	  if mod(i,2) == 0
	  y(i) = [];
	  end
end
	  display(y);	  
end
