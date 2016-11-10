function a = MonotoneIncrease(vec)
	% this function takes a vector and sees if it is monotonically
	% increasing.

  sz = size(vec,2);
  tf = true;
  for i =1:sz
    if i+1 == sz+1
    else
      if vec(i) > vec(i+1)
	tf = false;
      end
    end
  end
  fprintf("Output tf is %i\n",tf);
end
