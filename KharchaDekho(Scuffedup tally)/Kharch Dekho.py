from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import messagebox as mb
from tkinter import simpledialog
import os
from os import path
entry=l=ok=entry2=ok2=l2=tp=lab=label=''
def user():
    global entry2,l2,ok2
    path3=open('data.txt','r')
    c=path3.read()
    directory='Kharcha Dekho'
    sub_path=os.path.join(c, directory)
    d=entry2.get()
    main_sub_path=os.path.join(sub_path, d)
    mode = 0o666
    os.mkdir(main_sub_path,mode)
    entry2.destroy()
    l2.destroy()
    ok2.destroy()
    showinfo('USER', 'USER SUCCESSFULLY CREATED')
    res = mb.askquestion('Enter User', 'Do you want to enter new created user now?')
    if res == 'yes':
        pass
def open_user():
    global  tp, lab,label
    l1=Label(root,text="Your Users Are: ",bg="yellow")
    l1.config(font=("Courier", 14))
    root.configure(background='yellow')
    p2 = open("data.txt", "rt")
    p3 = p2.read()
    p2.close()
    directory = 'Kharcha Dekho'
    sub_path = os.path.join(p3, directory)


    dirs = [name for name in os.listdir(sub_path) if os.path.isdir(os.path.join(sub_path, name))]
    label = Listbox(root, bg='yellow', font=20)
    for item in dirs:
        label.insert(END, item)

    tp = Button(text='Open User', command=open2, bd=10, bg='red')

    lab = Label(text='Users are below:', bg='yellow', bd=10, font=10)
    lab.pack(side='top', anchor='nw' )
    label.pack(anchor='center', fill=BOTH)
    tp.pack(anchor='center')
    MenuBar.destroy()
def open2():
    global label,tp,lab
    user=label.get(ANCHOR)
    label.destroy()
    tp.destroy()
    lab.destroy()
    print(user)
def create_user():
    global entry2, l2, ok2
    l2= Label(root, text="Enter User Name ",bg='yellow')
    l2.grid(row=2,padx=10,pady=10)
    entry2 = Entry(root, width="50")
    entry2.grid(row=2,column=1,padx=2,pady=10,ipady=3)
    ok2=Button(root,text='ok',command=user,bg='yellow')
    ok2.grid(row=2, column=2, padx=2, pady=10, ipady=3)

def create_folder():
    path=open('data.txt','r')
    a=path.read()
    directory='Kharcha Dekho'
    main_path = os.path.join(a, directory)
    mode = 0o666
    os.mkdir(main_path,mode)
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="Create", command=create_user)
    FileMenu.add_command(label="Open", command=open_user)
    FileMenu.add_command(label="Exit", command=exit)
    MenuBar.add_cascade(label="File", menu=FileMenu)
    root.config(menu=MenuBar)
def setup():

    global entry,l,ok
    l= Label(root, text="Enter location to save file: ",bg='yellow')
    l.grid(row=4,padx=10,pady=10)
    entry = Entry(root, width="50")
    entry.insert(END, 'C:\\')
    entry.grid(row=4, column=1, padx=2, pady=10, ipady=3)
    ok=Button(root,text='ok',command=setup_runner,bg='yellow')
    ok.grid(row=4, column=3, padx=2, pady=10, ipady=3)

def setup_runner():
    global entry,l,ok
    d=entry.get()
    f=open("data.txt","wt")
    if d!=None:
        p=f.write(d)
    f.close()
    entry.destroy()
    l.destroy()
    ok.destroy()
    create_folder()
def exit():
    root.destroy()
def main():
    root=Tk()
    root.title("Kharcha Dekho")
    root.attributes("-fullscreen", True)
    root.configure(background='yellow')
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="Create", command=create_user)
    FileMenu.add_command(label="Open", command = open_user)
    FileMenu.add_command(label = "Exit", command = exit)
    MenuBar.add_cascade(label = "File", menu=FileMenu)
    root.config(menu=MenuBar)
    root.mainloop()
if __name__ == '__main__':
    root=Tk()
    root.title("Kharcha Dekho")
    root.attributes("-fullscreen", True)
    root.configure(background='yellow')
    try:
        f=open('1sttime.txt','r')
        f.close()
        MenuBar = Menu(root)
        FileMenu = Menu(MenuBar, tearoff=0)
        FileMenu.add_command(label="Create", command=create_user)
        FileMenu.add_command(label="Open", command=open_user)
        FileMenu.add_command(label="Exit", command=exit)
        MenuBar.add_cascade(label="File", menu=FileMenu)
        root.config(menu=MenuBar)

    except:
        f=open('1sttime.txt','x')
        f.close()
        setup()


    root.mainloop()