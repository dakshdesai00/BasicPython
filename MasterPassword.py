from tkinter import *
import random
char_list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','a','s','d','f','g','h','j','k','l','z',
 'x','c','v','b','n','m','q','w','e','r','t','y','u','i','o','p']
b1=b2=b3=b4=b5=b6=b7=l1=l2=entry1=scrollbar=password=''
listbox=''
def newpass():
    global b1,b2,b3,b4,b5,l1,entry1,char_list
    b1.destroy()
    b2.destroy()
    b3.destroy()
    l1.destroy()
    l1= Label(root, text="Password For:",bg='cyan')
    l1.grid(row=0,padx=10,pady=10)
    entry1 = Entry(root, width="50")
    entry1.grid(row=0,column=1,padx=5,pady=10,ipady=3)
    b4=Button(root,text="Ok",bg='black',fg='white',command=ok)
    b4.grid(row=0,column=2)
    b5=Button(root,text="Quit Current Mode",bg='black',fg='white',command=main)
    b5.place(x=210,y=250)
    root.configure(background='Cyan')
def delpass():

    global b1, b2, b3, b4, b5,b6, l1, entry1, char_list,listbox,scrollbar
    b1.destroy()
    b2.destroy()
    b3.destroy()
    l1.destroy()
    l1=Label(root,text="Select Password and press delete button below ",bg="Red")
    l1.config(font=("Courier", 14))
    l1.pack()
    b5=Button(root,text="Quit Current Mode",bg='black',fg='white',command=main)
    b5.place(x=230,y=273)
    b6=Button(root,text="Delete",bg='black',fg='white',command=deltext)
    b6.place(x=180,y=273)
    f1 = open('pass.txt', 'r')
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=BOTH)
    # print(f1.read())
    listbox = Listbox(root, bg='Red', font=('Times', 14))
    for x in f1:
        listbox.insert(END, x)
    listbox.config(yscrollcommand=scrollbar.set)
    listbox.pack(fill=X, expand=YES)
    scrollbar.config(command=listbox.yview)
    root.configure(background='Red')

def deltext():
    global listbox
    a=listbox.get(ANCHOR)
    print(a)
    f=open('pass.txt','w+')
    with open("pass.txt", "r") as f:
        lines = f.readlines()
    with open("pass.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != a:
                f.write(line)
    main()
def openpass():
    global b1, b2, b3, b4, b5, l1, entry1, char_list
    b1.destroy()
    b2.destroy()
    b3.destroy()
    l1.destroy()
    l1=Label(root,text="Your Passwords are: ",bg="Lime Green")
    l1.config(font=("Courier", 14))
    l1.pack()
    f1=open('pass.txt','r')
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=BOTH)
    #print(f1.read())
    listbox=Listbox(root,bg='Lime Green',font=('Times', 14))
    for x in f1:
        listbox.insert(END, x)
    listbox.config(yscrollcommand=scrollbar.set)
    listbox.pack(fill=X,expand=YES)
    scrollbar.config(command=listbox.yview)
    root.configure(background='Lime Green')
    b5=Button(root,text="Quit Current Mode",bg='black',fg='white',command=main)
    b5.place(x=200,y=273)
def ok():
    global b1, b2, b3, b4, b5,b6,b7, l1,l2, entry1, char_list,password

    dubpassword=random.choices(char_list,k=10)
    password = ' '.join([str(elem) for elem in dubpassword])
    l2=Label(root,text='Your password is: '+password,bg='cyan')
    l2.config(font=("Courier", 15))
    l2.place(x=10,y=100)
    l3=Label(root,text="Did You Like Password?",bg='cyan')
    l3.config(font=("Courier", 15))
    l3.place(x=50,y=120)
    b6=Button(root,text="Yes",bg='black',fg='white',command=save)
    b6.place(x=50,y=150)
    b7=Button(root,text="No",bg='black',fg='white',command=ok)
    b7.place(x=80,y=150)
def save():
    global b1, b2, b3, b4, b5,b6,b7, l1,l2, entry1, char_list
    f=open('pass.txt','a+')
    f.write('Password for: '+entry1.get()+' is '+password+'\n')
    f.close()
    main()
def main():
    global b1, b2, b3, b4, b5, l1, entry1, char_list,root
    root.destroy()
    root = Tk()
    root.title("MasterPassword-DakshIndustries")
    root.geometry("500x300")
    root.configure(background='yellow')

    b1=Button(text='Add New Password',command=newpass,bg='blue')
    b1.grid(row=4,column=1)
    b2=Button(text='See Created Password',command=openpass,bg='blue')
    b2.grid(row=4,column=2)
    b3=Button(text='Delete Old Password',command=delpass,bg='blue')
    b3.grid(row=4,column=3)
    l1 = Label(root,
               text='This is a software that helps you to manage passwords and create big and most secure passwords.',
               bg='yellow',wraplength=200)
    l1.config(font=("Courier", 15))
    l1.place(x=50,y=50)
    root.resizable(width=False, height=False)
    root.mainloop()

    delpass()
if __name__ == '__main__':
    root = Tk()
    root.title("MasterPassword-DakshIndustries")
    root.geometry("500x300")
    root.configure(background='yellow')

    b1=Button(text='Add New Password',command=newpass,bg='blue')
    b1.grid(row=4,column=1)
    b2=Button(text='See Created Password',command=openpass,bg='blue')
    b2.grid(row=4,column=2)
    b3=Button(text='Delete Old Password',command=delpass,bg='blue')
    b3.grid(row=4,column=3)
    l1 = Label(root,
               text='This is a software that helps you to manage passwords and create big and most secure passwords.',
               bg='yellow',wraplength=200)
    l1.config(font=("Courier", 15))
    l1.place(x=50,y=50)
    root.resizable(width=False, height=False)
    root.mainloop()
