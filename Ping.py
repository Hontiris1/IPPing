import os
import tkinter as tk
from tkinter import *
from tkinter.ttk import *

def close_window (root):
    root.destroy()

#This will add a new IP to the IPlist
def newip():
    data = e1.get()

    if data == "":
        print("Please enter an IP address")
    else:
        ipopen = open("IPlist.txt")
        with open('IPlist.txt', mode='a') as add:
            add.write("\n{}".format(data))
            print("Ip address {} has been added!".format(data))
            ipopen.close()
            label.grid_forget()

#This will read each line on the IPlist.txt file
def contents():
    ipopen = open("IPlist.txt")

    #Opens the IPlist.txt file and strips each of the lines so that we can read individually.
    with open("IPlist.txt", "r+") as ips_file:
        ips = [ip.strip() for ip in ips_file.readlines()]

    with open("IPlist.txt", mode='r') as read:
        for ip in ips:
            print(ip)
            #print(ip)
            #ipopen.seek(0)
            ipopen.close()
    return

def scanlist():
    import time
    progress = Progressbar(master, orient=HORIZONTAL, length=50, mode='indeterminate')
    progress.grid()
    master.update_idletasks()
    ipopen = open("IPlist.txt")

    #Opens the IPlist.txt file and strips each of the lines so that we can read individually.
    with open("IPlist.txt", "r+") as ips_file:
        ips = [ip.strip() for ip in ips_file.readlines()]
        progress['value'] = 0
        master.update_idletasks()
        time.sleep(0.5)

    #Read each line from the IPlist.txt file
    with open("IPlist.txt", "r") as available_ips_file:
        for ip in ips:  #Pings each line from the IPlist.txt file
            response = os.system('ping -a -n 1 {}'.format(ip))
            progress['value'] += 50
            master.update_idletasks()
            time.sleep(0.5)

            if response == 0:   #Up
                print("- Ip Address:", ip, 'is up!')
            elif response == 512:   #Down
                print("- IP Address:", ip, 'is down!')
            else:   #other error
                print("- Bad parameters or other error!")

    return progress.grid_forget()

master = tk.Tk()
master.title("IPPing")
master.geometry("350x100+900+300")

Label(master, text="___________").grid(row=1)
Label(master, text="Enter IP Address").grid(row=2)

e1 = tk.Entry(master)
e1.grid(row=2, column=1)

tk.Button(master,text='Add New IP', command=newip).grid(row=0,column=0,pady=2)
tk.Button(master,text='List of IPs', command=contents).grid(row=0,column=1,sticky=tk.SE,pady=2)
tk.Button(master,text='Ping all servers', command=scanlist).grid(row=0,column=2,sticky=tk.SE,pady=2)
tk.Button(master,text='Quit',command=master.quit).grid(row=0,column=3,pady=2)


tk.mainloop()
