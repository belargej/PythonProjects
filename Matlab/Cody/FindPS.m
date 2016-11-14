function a = FindPS(vec)
  a=false;
  inSize=size(vec,2);
  for i=1:inSize;
    square = vec(i)*vec(i);
    for j=1:inSize
      if vec(j)==square
	a=true;
	return;
      end
    end
  end
end
