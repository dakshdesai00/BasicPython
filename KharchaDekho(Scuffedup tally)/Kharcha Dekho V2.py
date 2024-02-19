from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import messagebox as mb
from tkinter import simpledialog
import os
from os import path
from pynput import keyboard
from PIL import Image,  ImageTk
pressed=False
entry=l=ok=entry2=ok2=l2=tp=lab=label=canvas=entry3=quitcalc=calc_label=''
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
    global entry2, l2, ok2,canvas
    canvas.destroy()
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
    root.attributes("-fullscreen", True)
    MenuBar.add_cascade(label="File", menu=FileMenu)
    root.config(menu=MenuBar)
    showinfo('Restart Needed','Press ok and then restart manually.')
    root.destroy()
def calculator():
    global pressed,content,entry3,quitcalc,calc_label

    if pressed==False:
        calc_label=Label(root,text='Calculator',font=50,bg='yellow')
        calc_label.pack(side=BOTTOM,anchor=SE)
        entry3=Entry(root,bg='grey', width=40,font=40)
        entry3.pack(side=BOTTOM,anchor=SE,ipady=20)

        def process(event=None):
            try:
                content = entry3.get()

                entry3.delete("0", "end")
                entry3.insert( END,str(eval(content)) )
            except:
                showinfo('Error','Enter Number Perfectly.')

        entry3 .bind('<Return>', process)
        quitcalc=Button(root,text='               Close Calc               ',command=quitcalc2,bg='yellow')
        quitcalc.pack(side=BOTTOM,anchor=SE)
        pressed=True
def quitcalc2():
    global pressed,entry3,calc_label,quitcalc
    pressed=False
    entry3.destroy()
    calc_label.destroy()
    quitcalc.destroy()
def setup():
    f = open('fullscreen.txt', 'x')
    f.close()
    global entry,l,ok
    l= Label(root, text="Enter location to save data.Click ok for default location: ",bg='yellow')
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

    if path.exists("fullscreen.txt")==True:
        root.attributes("-fullscreen", True)
        root.title("Kharcha Dekho")
        canvas = Canvas(root, width=300, height=300)
        canvas.pack(side='bottom',anchor=W)
        img = PhotoImage(file="KharchaDekho.png")
        canvas.create_image(20, 20, anchor=NW, image=img)
        calc=Button(root,text='Calculator',bg='yellow',command=calculator,bd=10)
        calc = canvas.create_window(10, 10, anchor=NW, window=calc)
    else:
        root.title("Kharcha Dekho(Setup)")
        root.geometry('700x300')
        root.resizable(False, False)

    root.configure(background='yellow')

    try:

        f=open('1sttime.txt','r')
        f.close()
        MenuBar = Menu(root)
        FileMenu = Menu(MenuBar, tearoff=0)
        FileMenu.add_command(label="Create", command=create_user)
        FileMenu.add_command(label="Open", command=open_user)
        FileMenu.add_command(label="Exit", command=exit)
        MenuBar.add_cascade(label="USERS", menu=FileMenu)
        root.config(menu=MenuBar)

    except:

        f=open('1sttime.txt','x')
        f.close()
        setup()


    root.mainloop()
if __name__ == '__main__':
    root=Tk()

    if path.exists("fullscreen.txt")==True:
        root.attributes("-fullscreen", True)
        root.title("Kharcha Dekho")
        canvas = Canvas(root, width=300, height=300)
        canvas.pack(side='bottom',anchor=W)
        img = PhotoImage(file="KharchaDekho.png")
        canvas.create_image(20, 20, anchor=NW, image=img)
        calc=Button(root,text='Calculator',bg='yellow',command=calculator,bd=10)
        calc = canvas.create_window(10, 10, anchor=NW, window=calc)
    else:
        root.title("Kharcha Dekho(Setup)")
        root.geometry('700x300')
        root.resizable(False, False)

    root.configure(background='yellow')

    try:

        f=open('1sttime.txt','r')
        f.close()
        MenuBar = Menu(root)
        FileMenu = Menu(MenuBar, tearoff=0)
        FileMenu.add_command(label="Create", command=create_user)
        FileMenu.add_command(label="Open", command=open_user)
        FileMenu.add_command(label="Exit", command=exit)
        MenuBar.add_cascade(label="USERS", menu=FileMenu)
        root.config(menu=MenuBar)

    except:

        f=open('1sttime.txt','x')
        f.close()
        setup()


    root.mainloop()