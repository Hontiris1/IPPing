import os
import time
import tkinter as tk
from tkinter import HORIZONTAL
from tkinter.ttk import Progressbar


class GUIframework(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.scanning = tk.Label(self, text="Scanning all IPs...")
        self.newnoip = tk.Label(self, text="Please enter a valid IP/Domain")

    def newip(self):
        '''
        This function adds a new IP/Domain to the IPlist.TXT file.
        '''

        self.data = self.e1.get()
        data = self.data

        if data == "":
            print("Please enter a valid IP address")
            self.newnoip.grid(row=3, column=1)
        else:
            ipopen = open("IPlist.txt")
            with open('IPlist.txt', mode='a') as add:
                add.write("\n{}".format(data))
                print("Ip address {} has been added!".format(data))
                ipopen.close()
                self.newnoip.grid_forget()


    def contents(self):
        '''
        This function reads the IP/Domain on the IPlist.TXT file and outputs them.
        '''
        ipopen = open("IPlist.txt", "r+")

        # Opens the IPlist.txt file and strips each of the lines so that we can read individually.
        with open("IPlist.txt", "r+") as ips_file:
            ips = [ip.strip() for ip in ips_file.readlines()]

        with open("IPlist.txt", mode='r+') as read:
            for ip in ips:
                print(ip)
                # ipopen.seek(0)
                ipopen.close()


    def scanlist(self):
        '''
        This function reads all of the IPs/Domain on the IPlist.TXT then
        pings them individually and checks if they are UP/DOWN!
        '''
        self.scanning.grid(row=4, column=1)
        progress = Progressbar(self, orient=HORIZONTAL, length=50, mode='indeterminate')
        progress.grid(row=2, column=2)
        self.update_idletasks()
        ipopen = open("IPlist.txt")

        # Opens the IPlist.txt file and strips each of the lines so that we can read individually.
        with open("IPlist.txt", "r+") as ips_file:
            ips = [ip.strip() for ip in ips_file.readlines()]

        # Read each line from the IPlist.txt file
        with open("IPlist.txt", "r") as available_ips_file:
            for ip in ips:  # Pings each line from the IPlist.txt file
                response = os.system('ping -a -n 1 {}'.format(ip))
                progress['value'] += 20
                self.update_idletasks()
                time.sleep(0.5)

                if response == 0:  # Up
                    print("- Ip Address:", ip, 'is up!')
                elif response == 512:  # Down
                    print("- IP Address:", ip, 'is down!')
                else:  # other error
                    print("- Bad parameters or other error!")

        self.scanning.grid_forget()

        return progress.grid_forget()


    def close_window(self):
        root.destroy()
