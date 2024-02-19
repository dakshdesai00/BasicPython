from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import simpledialog
import os
import pickle
import sys
MenuBar=''
d=''
cname=''
label=''
b7=''
email=''
number=''
address=''
country=''
details=''
b1=b2=b3=b4=b5=b6=b7=''
l=''
p3=''
tp=''
company=''
root=''
lab=''
label=''
pressed=False
def newFile():
    root.configure(background='light green')
    b = simpledialog.askstring(title="Create",
                                  prompt="Enter company name: ")
    email = simpledialog.askstring(title="Email ID",
                                  prompt=f"Enter Email ID of {b}: ")
    number = simpledialog.askstring(title="Number",
                                  prompt=f"Enter phone number of {b}: ")
    address = simpledialog.askstring(title="Address",
                                  prompt=f"Enter Address of {b}:")
    country = simpledialog.askstring(title="Country",
                                  prompt=f"Enter country of origin of {b}:")
                                                            
    p2=open("data.txt","rt")
    p3=p2.read()
    p2.close()
    directory = b  
    parent_dir = p3
    if directory!=None:
        path = os.path.join(parent_dir, directory) 
        if not os.path.isdir(path):    
            os.mkdir(path) 
        #print("Directory '% s' created" % directory)   
        directory = b
        parent_dir = p3   
        mode = 0o666
        path = os.path.join(parent_dir, directory)  
        details={"name of company":b, "email":email, "number": number, "address":address,"country":country}
        with open(b+'//'+'details.txt','wb') as f:
            pickle.dump(details,f)
            
def openFile():
    global cname,l,tp,lab,MenuBar
    root.configure(background='yellow')
    p2=open("data.txt","rt")
    p3=p2.read()
    p2.close()                             
    dirs=[ name for name in os.listdir(p3) if os.path.isdir(os.path.join(p3, name) )]  
    l=Listbox(root,bg='pink',font=20)
    for item in dirs:
        l.insert(END, item)
    
    tp=Button(text='Open Company',command=open123,bd=20,bg='red')
     
    lab=Label(text='Company Names are below:',bg='light blue',bd=10,font=10)
    lab.pack(side='top',anchor='nw',)
    l.pack(anchor='center',fill=BOTH)
    tp.pack(anchor='center') 
    MenuBar.destroy()    
def open123():
    global l,p3,company,tp,lab
    root.configure(background='light blue')
    company=l.get(ANCHOR)
    l1_name=Label(root, text=company,width=13)
    b1=Button(root,text= "Company Info ",width=13, command=ci,activeforeground="red")
    b2=Button(root,text = " Import Data ",width=13, command=impda,activeforeground="red")
    b3=Button(root,text = "Balance Sheet",width=13, command=bs,activeforeground="red")
    b4=Button(root,text = "Profit & Loss",width=13, command=pl,activeforeground="red")
    b5=Button(root,text="     GST     ",width=13,command=gst,activeforeground="red")
    b6=Button(root,text="Exit Company  ",width=13,command=quitcom,activeforeground="red")
    isFile=os.path.isdir(os.path.join(p3,company)) 
    l.destroy()
    tp.destroy()
    lab.destroy()
    if isFile==True:
        showinfo("Open",f"Now everything you edit will be done in {os.path.join(p3,company)}.")
        #print("Done")
        l1_name.place(x=6,y=0)
        b1.place(x=6,y=30)
        b2.place(x=6,y=60)
        b3.place(x=6,y=90)
        b4.place(x=6,y=120)
        b5.place(x=6,y=150)
        b6.place(x=6,y=180)
        isFile=None
    else:
       showinfo("Open","Sorry this company does not exist :(")
def ci():
    global company,d,label,b1, pressed, b7,label
    name=company
    mianfile=open('data.txt').read()
    maindir=mianfile+'\\'+name+'\\'+'details.txt'
    with open(maindir,'rb') as f:
        info=pickle.load(f)
    if pressed==False:    
        nameofc=info['name of company']
        emailofc=info['email']
        numberofc=info['number']
        addressofc=info['address']
        countryofc=info['country']

        b7=Button(root,text="Edit Company Info",width=13,command=edit,activeforeground="red")  
        b7.place(x=6,y=210)  
        label=Label(root,text="Name of company:"+nameofc+"\n"+"Email Id:"+emailofc+'\n'+"PhoneNumber:"+numberofc+"\n"+"Address of company:"+addressofc+"\n"+"Country of origin:"+countryofc+"\n")
        label.config(font=("Courier", 24))
        label.place(x=450,y=100)
        
        root.update()
        pressed=True
def edit():
    global email,number,address,country,details,company,label,pressed
    email = simpledialog.askstring(title="Email ID",
                                  prompt=f"Enter new Email ID of {company}: ")
    number = simpledialog.askstring(title="Number",
                                  prompt=f"Enter new phone number of {company}: ")
    address = simpledialog.askstring(title="Address",
                                  prompt=f"Enter new Address of {company}:")
    country = simpledialog.askstring(title="Country",
                                  prompt=f"Enter new country of origin of {company}:")

    yes_or_no=simpledialog.askstring(title="Are you sure?",
                                  prompt=f" Are you sure you want to change the detais of {company}(yes or no):")
    if yes_or_no.lower()=='yes':
        mianfile=open('data.txt').read()
        maindir=mianfile+'\\'+company+'\\'+'details.txt'
        with open(maindir,'rb') as f:
            info=pickle.load(f)
        emailofc=info['email']
        numberofc=info['number']
        addressofc=info['address']
        countryofc=info['country']
                                
        details={"name of company":company, "email":email, "number": number, "address":address,"country":country}
        with open(company+'//'+'details.txt','wb') as f:
            pickle.dump(details,f)  
        #showinfo("To Save Info","Press Exit Company and then check 'Company Info' to see what is saved")  
        label.destroy()
        pressed=False
        ci()                            
def impda():
    global label, pressed, b7
    pressed=False
    label.destroy()
    try:
        b7.destroy()
    except:
        pass
    root.update()
def bs():
    global label, pressed, b7
    pressed=False
    label.destroy()
    try:
        b7.destroy()
    except:
        pass
    root.update()
def pl():
    global label, pressed, b7
    pressed=False
    label.destroy()
    try:
        b7.destroy()
    except:
        pass
    root.update()
def gst():
    global label, pressed, b7
    pressed=False
    label.destroy()
    try:
        b7.destroy()
    except:
        pass
    root.update()
def quitcom():
    global root, pressed
    root.configure(background='pink')
    pressed=False
    showinfo("Wait","Please wait for a second")
    root.destroy()
    root = Tk()
    root.title("Business Manager")
    root.geometry("1366x788")
    root.configure(background='pink')
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="Create", command=newFile)
    FileMenu.add_command(label="Open", command = openFile)
    FileMenu.add_command(label = "Exit", command = quitApp)
    MenuBar.add_cascade(label = "File", menu=FileMenu)
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About Business Manager", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)
    setup=Menu(MenuBar,tearoff=0)
    setup.add_command(label="Path of Company",command=setup1)
    MenuBar.add_cascade(label = "Setup", menu=setup)
    root.config(menu=MenuBar)
    root.mainloop()
def quitApp():
    root.destroy()  
def about():
    showinfo("Bussiness Manager","This is made by Mr.Daksh and Mr.Manan. For any issues contact 1234567890")
    #Add our phonenumber
def setup1():
    global d
    d=simpledialog.askstring(title="Path",prompt="Enter path to store companies data:") 
    f=open("data.txt","wt")
    if d!=None:
        p=f.write(d)
        #print(p)
    f.close()  

if __name__ == '__main__':
    
    root = Tk()
    root.title("Business Manager-DakshIndustries")
    root.geometry("1366x788")
    root.configure(background='pink')
    try:
        f=open('1sttime.txt','r')
        f.close()       
    except:
        f=open('1sttime.txt','x')
        f.close() 
        setup1()
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="Create", command=newFile)
    FileMenu.add_command(label="Open", command = openFile)
    FileMenu.add_command(label = "Exit", command = quitApp)
    MenuBar.add_cascade(label = "File", menu=FileMenu)
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About Business Manager", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)
    setup=Menu(MenuBar,tearoff=0)
    setup.add_command(label="Path of Company",command=setup1)
    MenuBar.add_cascade(label = "Setup", menu=setup)
    root.config(menu=MenuBar)
    root.mainloop()
