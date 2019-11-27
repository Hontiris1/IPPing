import os
import time
import tkinter as tk
from time import sleep
from tkinter import HORIZONTAL
from tkinter.ttk import Progressbar
from tkinter import messagebox
from os import startfile
from tkinter import scrolledtext


class IPfunctions(tk.Frame):
    """This class uses the tkinter frame, and is used on the GUI on main.py"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # self.configure(bg='grey')
        self.ipadded = tk.Label(self, text="IP has been added to IPlist.txt!", fg="green", font=("Arial Bold", 9))
        self.scan_done = tk.Label(self, text="All IPs are Up!", fg="green", font=("Arial Bold", 9))
        self.scan_down = tk.Label(self, text="One or more IPs are down!", fg="red", font=("Arial Bold", 9))
        self.scanning = tk.Label(self, text="Scanning IPlist.txt please wait...", fg="green", font=("Arial Bold", 9))
        self.newnoip = tk.Label(self, text="Please enter a valid IP/Domain", fg="red", font=("Arial Bold", 9))
        self.bad_ip = tk.Label(self, text="An IP has bad parameters", fg="red", font=("Arial Bold", 9))
        self.progress = Progressbar(self, orient=HORIZONTAL, length=70, mode='indeterminate')

    def newip(self):
        """
        This function adds a new IP/Domain to the IPlist.TXT file.
        """
        self.forget_labels()
        self.data = self.e1.get()

        if self.data == "":
            print("Please enter a valid IP address")
            self.no_ip = messagebox.showerror('IPPing', 'Please enter a valid IP address')
            self.newnoip.grid(row=3, column=1)
        else:
            ipopen = open("IPlist.txt", "a+")
            with open('IPlist.txt', mode='a') as add:
                add.write("{}\n".format(self.data))
                print("Ip address {} has been added!".format(self.data))
                self.forget_labels()
                self.ipadded.grid(row=5, column=1)

        return ipopen.seek(0), ipopen.close()

    def contents(self):
        """
        This function reads the IP/Domain on the IPlist.TXT file and outputs them.
        """
        self.forget_labels()
        ipopen = open("IPlist.txt")

        # Opens the IPlist.txt file and strips each of the lines so that we can read individually.
        with open("IPlist.txt", "r") as ips_file:
            ips = [ip.strip() for ip in ips_file.readlines()]

        with open("IPlist.txt", mode='r') as read:
            for ip in ips:
                print(ip)
                # ipopen.seek(0)

        return startfile("IPlist.txt"), ipopen.close()

    def reports(self):
        ipreport = open("IPreport.txt", "w+")
        self.forget_labels()
        return ipreport.close(), startfile("IPreport.txt")

    def scanlist(self):
        """
        This function reads all of the IPs/Domain on the IPlist.TXT then
        pings them individually and checks if they are UP/DOWN!
        """
        self.forget_labels()
        self.scanning.grid(row=4, column=1)
        self.progress.grid(row=2, column=2)
        ipopen = open("IPlist.txt")
        ipreport = open("IPreport.txt")

        # Opens the IPlist.txt file and strips each of the lines so that we can read individually.
        with open("IPlist.txt", "r") as ips_file:
            ips = [ip.strip() for ip in ips_file.readlines()]

        # Read each line from the IPlist.txt file
        with open("IPlist.txt", "r") as available_ips_file:
            for ip in ips:  # Pings each line from the IPlist.txt file
                response = os.system('ping -a -n 1 {}'.format(ip))
                self.progress['value'] += 20
                self.update_idletasks()
                time.sleep(0.8)

                if response == 0:  # Up
                    with open('IPreport.txt', mode='a') as add:
                        add.write("- IP: {} is UP!\n".format(ip))
                    print("- Ip Address:", ip, 'is up!')
                elif response <= 512:  # Down
                    with open('IPreport.txt', mode='a') as add:
                        add.write("- IP: {} is Down!\n".format(ip))
                    print("- IP Address:", ip, 'is down!')
                else:  # other error
                    with open('IPreport.txt', mode='a') as add:
                        add.write("- IP: {} (Error: Bad parameters or is Down!)\n".format(ip))
                    print("- Error: Bad parameters or is Down!")
                    self.bad_ip.grid(row=4, column=1)
                    # break

            if response == 0:
                self.scan_done.grid(row=4, column=1)
            else:
                self.scan_down.grid(row=4, column=1)
                print("- Error: Bad parameters or is Down!")

        return self.progress.grid_forget(), self.scanning.grid_forget(), ipreport.close(), \
               ipopen.close(), startfile("IPreport.txt")

    def forget_labels(self):
        return self.bad_ip.grid_forget(), self.ipadded.grid_forget(), self.newnoip.grid_forget(), \
               self.scanning.grid_forget(), self.scan_done.grid_remove(), self.scan_down.grid_remove()

    def close_window(self):
        self.destroy()
