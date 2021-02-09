a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
c=str(input("Enter sum or leave blank  for addition: "))
d=str(input("Enter divide or leave blank for addition: "))
if c=="sum":
    print(a+b)
elif d=="divide":
    print(a/b)   
else:
    print("User inputed nothing")     