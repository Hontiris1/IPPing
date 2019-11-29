import os
import time
import tkinter as tk
from time import sleep
from tkinter import HORIZONTAL
from tkinter.ttk import Progressbar
from tkinter import messagebox
from os import startfile
import socket
import datetime


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
        self.dupe_detected = tk.Label(self, text="Dupe IP/Domain detected", fg="red", font=("Arial Bold", 9))
        self.invalid_detected = tk.Label(self, text="Invalid IPv4/IPv6 detected", fg="red", font=("Arial Bold", 9))
        self.bad_ip = tk.Label(self, text="An IP has bad parameters", fg="red", font=("Arial Bold", 9))
        self.progress = Progressbar(self, orient=HORIZONTAL, length=70, mode='indeterminate')

    def checkip(self):
        """This function will check the IP entered by the user, it will make sure
        that its a proper IPv4 or IPv6 IP address then return a True or False"""
        self.forget_labels()
        try:
            socket.inet_aton(self.e1.get())
            print("[Debug] validIP Set to True")
            self.validip = True
        except socket.error:
            self.validip = False
            print("[Debug Error] validIP Set to False")
            self.invalid_detected.grid(row=3, column=1)

        return self.validip

    def checkduplicate(self):
        """This function checks for a duplicate IP or Domain on the IPlist.txt file then returns
        True or False"""
        self.forget_labels()
        ipopen = open("IPlist.txt", "r")

        with open("IPlist.txt", "r") as ip_file:
            ips = [ip.strip() for ip in ip_file.readlines()]

            for ip in ips:
                if self.e1.get() == ip:
                    self.dupeip = False
                    print("[Debug Error] Dup Found")
                    self.dupe_detected.grid(row=3, column=1)
                    break
                else:
                    self.dupeip = True

            print("[Debug] Dup not found")

        return self.dupeip, ipopen.seek(0), ipopen.close()

    def newip(self):
        """
         This function adds a new IP/Domain to the IPlist.TXT file.
         Before anything it will check that the IP/Domain has 15 or less characters.
         Then it will proceed to check if checkip and checkduplicate are both True.
         Once everything checks out and there is no issues the IP/domain will be added to IPlist.txt
         """
        self.forget_labels()
        self.checkip()
        self.checkduplicate()
        input_data = self.e1.get()
        ipopen = open("IPlist.txt")

        if len(input_data) > 15 or "":
            print("[Debug Error] Input data lenght was more than 15 characters!")
            return self.newnoip.grid(row=5, column=1), ipopen.seek(0)
        else:
            print("[Debug] Input data lenght is less than 15 characters")

        try:
            input_data = int(input_data) or float(input_data)
            if self.validip and self.dupeip:
                with open('IPlist.txt', mode='a') as add_ip:
                    add_ip.write("{}\n".format(input_data))
                    self.forget_labels()
                    self.ipadded.grid(row=5, column=1)
                    print("[Debug] IP address {} has been added!".format(input_data))
            else:
                self.no_ip = messagebox.showerror('IPPing', 'Invalid IP or duplicate!')
                print("[Debug Error] Is not valid IPv4/IPv6 or is duplicate on IPlist.txt")
            print("[Debug] User input is int ")
        except ValueError:
            input_data = str(input_data)
            print("[Debug] User input is Str")
            if "." in input_data and self.dupeip:
                with open('IPlist.txt', mode='a') as add_domain:
                    add_domain.write("{}\n".format(input_data))
                    print("Domain {} has been added!".format(input_data))
                    self.forget_labels()
                    self.ipadded.grid(row=5, column=1)
            else:
                self.no_ip = messagebox.showerror('IPPing', 'Domain address is incorrect or there is a duplicate!')
                self.newnoip.grid(row=5, column=1)
                print("[Debug Error] Incorrect Domain entry or is duplicate!")

        return ipopen.seek(0)

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

        return ipopen.seek(0), ipopen.close(), startfile("IPlist.txt")

    def reports(self):
        ipreport = open("IPreport.txt", "w+")
        self.forget_labels()
        return ipreport.close(), startfile("IPreport.txt")

    def timestamp(self, fname, fmt='%Y-%m-%d-%H-%M-%S_{fname}'):
        return datetime.datetime.now().strftime(fmt).format(fname=fname)

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
                self.response = os.system('ping -a -n 1 {}'.format(ip))
                self.progress['value'] += 20
                self.update_idletasks()
                time.sleep(0.8)

                if self.response == 0:  # Up
                    with open(self.timestamp('Ping Reports.txt'), 'w') as add:
                        add.write("- IP: {} is UP!\n".format(ip))
                    with open('IPreport.txt', mode='w') as add:
                        add.write("- IP: {} is UP!\n".format(ip))
                    print("- Ip Address:", ip, 'is up!')
                elif self.response <= 512:  # Down
                    with open(self.timestamp('Ping Reports.txt'), 'w') as add:
                        add.write("- IP: {} is Down!\n".format(ip))
                    with open('IPreport.txt', mode='w') as add:
                        add.write("- IP: {} is Down!\n".format(ip))
                    print("- IP Address:", ip, 'is down!')
                else:  # other error
                    with open(self.timestamp('Ping Reports.txt'), 'w') as add:
                        add.write("- IP: {} (Error: Bad parameters or is Down!)\n".format(ip))
                    with open('IPreport.txt', mode='w') as add:
                        add.write("- IP: {} (Error: Bad parameters or is Down!)\n".format(ip))
                        print("- Error: Bad parameters or is Down!")
                        self.bad_ip.grid(row=4, column=1)
                        break

            if self.response == 0:
                self.scan_done.grid(row=4, column=1)
            else:
                self.scan_down.grid(row=4, column=1)
                print("- Error: Bad parameters or is Down!")

        return self.progress.grid_forget(), self.scanning.grid_forget(), ipreport.close(), \
               ipopen.close(), startfile("IPreport.txt")

    def forget_labels(self):
        return self.bad_ip.grid_forget(), self.ipadded.grid_forget(), self.newnoip.grid_forget(), \
               self.scanning.grid_forget(), self.scan_done.grid_remove(), self.scan_down.grid_remove(), \
               self.invalid_detected.grid_forget(), self.dupe_detected.grid_forget()

    def close_window(self):
        self.destroy()
