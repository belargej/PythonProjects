function a =STB_less(tiles,rows,cols)
  a=zeros(rows,cols);
  index=[1:size(tiles,2)];
  while size(tiles,2)>rows*cols
    [z,b]=min(tiles);
    index(b)=[];
    tiles(b)=[];
  end
  for i=1:rows*cols
    a(i)=index(i);
    display(a);
  end
end
