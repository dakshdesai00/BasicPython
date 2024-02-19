import os
import time
import keyboard as k
senddir = input('Enter directory to send files: ')
codePath = "C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Windows PowerShell\\Windows PowerShell"
os.startfile(codePath)
time.sleep(2)
k.write("cd " + senddir)
k.press_and_release('enter')
time.sleep(0.5)
k.write('py -m http.server 8000')
k.press_and_release('enter')