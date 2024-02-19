a=0
b=''
c=0

import time
print("This Quiz is made by Daksh on the account of Teacher's day.Quiz begins in 5 seconds")
time.sleep(5)
if a==0:
    print("1.In which year did KVIS opened?")
    b=input("Answer: ")
    if b=='2002':
        a=a+1
        c=c+1
    else:
        a=a+1
        print('Wrong Answer') 
       
if a==1:
    print("2.Since when India is celebrating Teachers' Day?")
    b=input("Answer: ")
    if b=='1962':
        a=a+1
        c=c+1
    else:
        a=a+1
        print('Wrong Answer')

if a==2:
    print('3.Who said that “Teaching is not a profession, a way of life”')
    b=input("Answer: ")
    if b=='Narendra Modi':
        a=a+1
        c=c+1
    else:
        a=a+1 
        print('Wrong Answer')

if a==3:
    print("4.When Dr. Radhakrishnan became the President of India")
    b=input("Answer: ")
    if b=='1962':
        a=a+1
        c=c+1
    else:
        a=a+1
        print('Wrong Answer')
if a==4:
    print("5. In 1931 Dr. Sarvapalli Radhakrishnan became the Vice-Chancellor of which University?")
    b=input("Answer: ")
    if b=='Andhra University':
        a=a+1
        c=c+1
    else:
        a=a+1  
        print('Wrong Answer')

if a==5:
    print("6.Guess who was the teacher of Lord Krishna?")
    b=input("Answer: ")
    if b=='Sandipani Muni':
        a=a+1
        c=c+1
    else:
        a=a+1 
        print('Wrong Answer')

if a==6:
    print("7.In which subject Dr. Radhakrishnan had done his Post Graduation?")
    b=input("Answer: ")
    if b=='Philosophy':
        a=a+1
        c=c+1
    else:
        a=a+1 
        print('Wrong Answer')
if a==7:
    print("8.How is Teachers Day originated?")
    b=input("Answer: ")
    if b=='Birthday of Radhakrishna':
        a=a+1
        c=c+1
    else:
        a=a+1  
        print('Wrong Answer')

if a==8:
    print("9.Which among the following body inaugurated 'World Teachers Day'?")
    b=input("Answer: ")
    if b=='UNESCO':
        a=a+1
        c=c+1
    else:
        a=a+1  
        print('Wrong Answer')

if a==9:
    print("10.In which year was the University Education Commission formed?")
    b=input("Answer: ")
    if b=='1948':
        a=a+1
        c=c+1
    else:
        a=a+1
        print('Wrong Answer')    
    
print("Your score is: "+str(c)+"/10")
if c<10:   
    print("Right answers for-1:2002, 2:1962 ,3:Narendra Modi ,4:1962 ,5:Andhra University ,6:Sandipani Muni ,7:Philosophy ,8:Birthday of Radhakrishna ,9:UNESCO ,10:1948")
time.sleep(100000)     
