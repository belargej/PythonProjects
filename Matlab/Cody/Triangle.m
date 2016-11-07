function a = Triangle(n)
				% Given a number n this function
				% will spit out the triangle number.
				% Maybe it will also spit out the triangle.
  number=n;
  sum_val=0;
  for i= 1:number
    x = [1:i];
    display(x);
    clear x;
    sum_val = sum_val+i;
  end
  display(sum_val);
end
