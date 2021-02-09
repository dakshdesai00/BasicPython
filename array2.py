x=[]
a=int(input("Enter number of elements:"))
for i in range(a):
    c=input("Elements:")
    x.append(c)
print(x)   

add=0
n=0
for h in range(0,a):
    add=int(x[h]) +add
    if int(x[h])<0:
        n=int(x[h])+n
print(n)  
print(add)   