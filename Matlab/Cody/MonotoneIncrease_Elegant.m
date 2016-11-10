function a = MonotoneIncrease_Elegant(vec)
	     % this is the nice way to determine if a vector increases
	     % monotonically.
  if all(diff(vec)>0)==1
    tf = true;
  else
    tf = false;
  end

  fprintf("Output is %i\n",tf);

  
end
  
