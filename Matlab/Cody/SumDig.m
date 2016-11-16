function b=SumDig(n)

  val=power(2,n);
  s=num2str(val);
  digits=size(s,2);
  b=0;
  for i=1:digits
    b=b+str2double(s(i));
  end
end
