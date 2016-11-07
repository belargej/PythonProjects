function a = CleanUp(x)
				% Take a vector and replace all
				% elements >10 or <0 with NaN.
  sz = size(x,2);
  display(sz);
  for i=1:sz
    if x(i)<0 || x(i)>10
      fprintf("x(%i) = %d\n", i, x(i));
      x(i) = NaN;
    end
  end

  display(x);

end
