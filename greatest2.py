a=int(input("enter the 1st number"))
b=int(input("enter the 2nd number"))
c=int(input("enter the 3rd number"))
if(a>b):
    if(a>c):
        print("a is greater than b is greater than c")
    else:
        print("c is greater than a greater than b")
else:
    if(b>c):
        print("b is greater than c grater than a")
    else:
        print("c is gratest than b greater than a")
