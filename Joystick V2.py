from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import simpledialog
import threading
import serial
import serial.tools.list_ports
import keyboard as k
import sys
import time
entry2=entry3=entry4=entry5=''
l2=l3=l4=l5=''
com=a=w=s=d=b=''
def c():
    global l2,l3,l4,l5,l1,b
    global entry2,entry3,entry4,entry5
    a.destroy()

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

    def get_ports():
        ports = serial.tools.list_ports.comports()

        return ports

    def findArduino(portsFound):
        commPort = 'None'
        numConnection = len(portsFound)

        for i in range(0, numConnection):
            port = foundPorts[i]
            strPort = str(port)

            if 'CH340' or 'Arduino' in strPort:
                splitPort = strPort.split(' ')
                commPort = (splitPort[0])

        return commPort

    foundPorts = get_ports()
    connectPort = findArduino(foundPorts)

    if connectPort != 'None':
        ser = serial.Serial(connectPort, baudrate=9600, timeout=1)
        showinfo("CONFIGURATOR", 'Connected to ' + connectPort)
        print('Connected to ' + connectPort)
        l6 = Label(root,
                   text='Your confirguation has started you can now use your arduino joystick.If you want to stop using joystick than close the software first and then remove controller',
                   bg='yellow', wraplength=500)
        l6.config(font=("Courier", 15))
        l6.pack()
    else:

        showinfo('CONFIGURATOR','CONTROLLER NOT CONNECTED!!! CLOSE SOFTWARE TO TRY AGAIN..')

        sys.exit()


    print('DONE')
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






def s():
    global l2, l3, l4, l5,b,w,a,s,d,com
    global entry1, entry2, entry3, entry4, entry5
    b.destroy()
    w= entry2.get()
    a = entry3.get()
    d =entry4.get()
    s = entry5.get()

    entry2.destroy()
    entry3.destroy()
    entry4.destroy()
    entry5.destroy()

    l2.destroy()
    l3.destroy()
    l4.destroy()
    l5.destroy()

    t2 = threading.Thread(target=main2)

    t2.start()

root = Tk()
root.title("JOYSTICK CONFIGURATOR-DakshIndustries")
root.geometry("600x300")
root.configure(background='yellow')
a=Button(text='Start Configuration',command=c,bg='blue')
a.pack(anchor='center')
root.resizable(width=False, height=False)
root.mainloop()