print("Fibonacci Sequence!")
a=0
b=1
count=0
max_count=int(input("How far do you want to go?? "))
while count < max_count:
    count = count+1
    print(a,end=" ") #end keeps from printing a new line.
    old_a = a
    a=b
    b= old_a+b
print()
