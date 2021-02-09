import math
print("Welcome")
print("User:Daksh Desai")
p=float(input("Enter marks of physics"))
c=float(input("Enter marks of ckemistry"))
m=float(input("Enter marks of biology"))
avg=(p+c+m)/3
print(str(avg))
print(math.floor(avg))
print(str(math.ceil(avg)))
