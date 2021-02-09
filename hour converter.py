s=int(input("Enter Seconds: "))
m=s//60
hour=s//3600
a=s%60
print('Time is: '+str(hour)+":"+str(m)+":"+str(a))
