import random
import pyautogui
import string
import threading
char=string.printable

char_list=list(char)
password= pyautogui.password("Enter Password: ")
found=False
def crack():
    global found
    guess_password=''
    while(guess_password!=password):
        guess_password=random.choices(char_list,k=len(password))
        print("<<============="+str(guess_password)+"=============>>")
        if (guess_password==list(password)):
            print("Your password is: "+''.join(guess_password))
            found=True
            break

for x in range(100):
    t=threading.Thread(target=crack)
    print("thread"+str(x)+"made")
    t.start()
    print("thread"+str(x)+"started")


if found==True:
    exit()
