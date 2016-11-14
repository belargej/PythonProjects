function a=WeightedAve(val,weights)

  sz=size(val,2);
  sum=0;
  for i=1:sz
    sum=sum+val(i)*weights(i);
  end
  a=sum/sz;
end
