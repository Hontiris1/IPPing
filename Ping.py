import os
import tkinter as tk

def close_window (root):
    root.destroy()

#This will add a new IP to the IPlist
def newip():
    data = e1.get()

    if data == "":
        print("You must enter an IP address")
    else:
        ipopen = open("IPlist.txt")
        with open('IPlist.txt', mode='a') as add:
            add.write("\n{}".format(data))
            ipopen.close()

#This will read each line on the IPlist.txt file
def contents():
    ipopen = open("IPlist.txt")

    #Opens the IPlist.txt file and strips each of the lines so that we can read individually.
    with open("IPlist.txt", "r+") as ips_file:
        ips = [ip.strip() for ip in ips_file.readlines()]

    with open("IPlist.txt", mode='r') as read:
        for ip in ips:
            #print(ip)
            ipopen.seek(0)
            ipopen.close()
    return print(ip)

def scanlist():
    ipopen = open("IPlist.txt")

    #Opens the IPlist.txt file and strips each of the lines so that we can read individually.
    with open("IPlist.txt", "r+") as ips_file:
        ips = [ip.strip() for ip in ips_file.readlines()]

    #Read each line from the IPlist.txt file
    with open("IPlist.txt", "r") as available_ips_file:
        for ip in ips:
            #Pings each line from the IPlist.txt file
            response = os.system('ping -a 1 {}'.format(ip))

            if response == 0:  # 512/DOWN value - 0/UP value
                # Up
                print("- Ip Address:", ip, 'is up!')
            elif response == 512:
                #down
                print("- IP Address:", ip, 'is down!')
            else:
                #other error
                print("- Bad parameters or other error!")

master = tk.Tk()
master.title("IPPing")
master.geometry("350x100+900+300")

tk.Label(master,text="IP Address").grid(row=0)
e1 = tk.Entry(master)
e1.grid(row=0, column=1)

tk.Button(master,text='Ping all servers', command=scanlist).grid(row=2,column=0,sticky=tk.W,pady=4)
tk.Button(master,text='Add New IP', command=newip).grid(row=2,column=1,sticky=tk.W,pady=4)
tk.Button(master,text='List of IPs', command=contents).grid(row=2,column=2,sticky=tk.W,pady=4)
tk.Button(master,text='Quit',command=master.quit).grid(row=2,column=3,sticky=tk.W,pady=4)

tk.mainloop()
