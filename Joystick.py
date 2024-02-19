from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import simpledialog
import threading
import serial
import keyboard as k
entry1=entry2=entry3=entry4=entry5=''
l2=l3=l4=l5=''
com=a=w=s=d=b=''
def c():
    global l2,l3,l4,l5,l1,b
    global entry1,entry2,entry3,entry4,entry5
    a.destroy()
    l1= Label(root, text="Choose port(COM):",bg='cyan')
    l1.grid(row=0,padx=10,pady=10)
    entry1 = Entry(root, width="50")
    entry1.grid(row=0,column=1,padx=5,pady=10,ipady=3)
    l2= Label(root, text="Key pressed when joystick is forward:",bg='cyan')
    l2.grid(row=2,padx=10,pady=10)
    entry2 = Entry(root, width="50")
    entry2.grid(row=2,column=1,padx=2,pady=10,ipady=3)
    l3= Label(root, text="Key pressed when joystick is left:",bg='cyan')
    l3.grid(row=3,padx=10,pady=10)
    entry3 = Entry(root, width="50")
    entry3.grid(row=3,column=1,padx=2,pady=10,ipady=3)
    l4= Label(root, text="Key pressed when joystick is right:",bg='cyan')
    l4.grid(row=4,padx=10,pady=10)
    entry4 = Entry(root, width="50")
    entry4.grid(row=4,column=1,padx=2,pady=10,ipady=3)
    l5= Label(root, text="Key pressed when joystick is backward:",bg='cyan')
    l5.grid(row=5,padx=10,pady=10)
    entry5 = Entry(root, width="50")
    entry5.grid(row=5,column=1,padx=2,pady=10,ipady=3)
    b=Button(text='Start Configuration',command=s,bg='blue')
    b.grid(row=6, column=1, padx=20, pady=10, ipady=3)
def main2():
    global w, a, s, d, com
    ser = serial.Serial(com, 9600)
    while True:
        h = ser.readline()
        b2 = h.decode(encoding="utf8", errors='ignore')
        string = b2.rstrip()
        # print(string)
        if string == 'a':
            k.press(a)
        if string == 'd':
            k.press(d)
        if string == 'w':
            k.press(w)
        if string == 's':
            k.press(s)
        if string == 'nopress':
            k.release(w)
            k.release(a)
            k.release(s)
            k.release(d)
def main():



        l6 = Label(root,
                   text='Your confirguation has started you can now use your arduino joystick.If you want to stop using joystick than remove controller first and then close software',
                   bg='yellow', wraplength=500)
        l6.config(font=("Courier", 15))
        l6.pack()

def s():
    global l2, l3, l4, l5, l1,b,w,a,s,d,com
    global entry1, entry2, entry3, entry4, entry5
    b.destroy()
    com=entry1.get()
    w= entry2.get()
    a = entry3.get()
    d =entry4.get()
    s = entry5.get()
    entry1.destroy()
    entry2.destroy()
    entry3.destroy()
    entry4.destroy()
    entry5.destroy()
    l1.destroy()
    l2.destroy()
    l3.destroy()
    l4.destroy()
    l5.destroy()
    t1=threading.Thread(target=main)
    t2 = threading.Thread(target=main2)
    t1.start()
    t2.start()

root = Tk()
root.title("JOYSTICK CONFIGURATOR-DakshIndustries")
root.geometry("600x300")
root.configure(background='yellow')
a=Button(text='Start Configuration',command=c,bg='blue')
a.pack(anchor='center')
root.resizable(width=False, height=False)
root.mainloop()