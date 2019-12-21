import os
import time
import tkinter as tk
import os.path
import socket
import datetime

from os import startfile
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Progressbar


class IPfunctions(tk.Frame):
    """This class uses the tkinter frame, and is used on the GUI on main.py"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        #  Progress bar for the scanning process
        self.progress = Progressbar(self, orient=tk.HORIZONTAL, length=70, mode='indeterminate')

        #  Settings
        self.default_scan = True
        self.validip = False
        self.dupeip = False

    """--------------------------------------Functions for the IPPing main features-------------------------"""

    def scanlist(self):

        """
        This function reads all of the IPs/Domain on the IPlist.TXT then
        pings them individually and checks if they are UP/DOWN!
        """

        notifications = tk.Label(self, text="Thank you for using IPPing!", fg="green", font=("Arial Bold", 9))

        # This checks if IPlist.txt is empty or not
        if os.stat("IPlist.txt").st_size == 0:
            notifications['text'] = 'IPlist.txt is empty!'
            notifications['fg'] = 'red'
            notifications.grid(row=4, column=1)
            self.after(2000, notifications.destroy)
            return print("[IPPing] No IP/Domain found inside IPlist.txt")
        else:
            print("[IPPing] IPlist.txt contains IPs proceeding...")

        notifications['text'] = 'Scanning IPlist.txt please wait...'
        notifications['fg'] = 'green'
        notifications.grid(row=4, column=1)
        self.progress.grid(row=2, column=2)  # <----

        report = []
        responses = []

        self.defaultscancheck()

        with open('IPreport.txt', mode='a') as add:
            # add.write("{}\n".format(self.timestamp2))
            add.write("----------------------\n")
            add.write(self.timestamp2() + "\n")
            add.write("Recent Reports\n")
            add.write("----------------------\n")

        if self.default_scan:
            # Opens the IPlist.txt file and strips each of the lines so that we can read individually.
            with open("IPlist.txt", "r") as ips_file:
                ips = [ip.strip() for ip in ips_file.readlines()]
        else:
            with open("{}".format(self.customscandir()), "r") as ips_file:
                ips = [ip.strip() for ip in ips_file.readlines()]

        with open("{}".format(self.customscandir()), "r") as available_ips_file:
            for ip in ips:  # Pings each line from the IPlist.txt file
                self.response = os.system("ping -a -n 1 {}".format(ip))
                self.progress['value'] += 20
                self.update_idletasks()
                time.sleep(0.8)

                if self.response == 0:  # Up
                    with open('IPreport.txt', mode='a') as add:
                        add.write("- IP: {} is UP!\n".format(ip))
                        report.append("- IP: {} is UP!\n".format(ip))
                        print("- Ip Address:", ip, 'is up!')
                        responses.append(self.response)
                elif self.response == 1:  # 512 Down
                    with open('IPreport.txt', mode='a') as add:
                        add.write("- IP: {} is Down!\n".format(ip))
                        report.append("- IP: {} is Down!\n".format(ip))
                        print("- IP Address:", ip, 'is down!')
                        responses.append(self.response)
                else:  # other error
                    with open('IPreport.txt', mode='a') as add:
                        add.write("- IP: {} (Error: Bad parameters or is Down!)\n".format(ip))
                        report.append("- IP: {} (Error: Bad parameters or is Down!".format(ip))
                        print("- Error: Bad parameters or is Down!")
                        notifications['text'] = 'An IP has bad parameters'
                        notifications['fg'] = 'red'
                        responses.append(self.response)
                        break

        with open(self.timestamp(" Ping_Reports.txt"), 'w+') as add:
            for ip in report:
                add.write(ip)

        if 1 in responses:
            notifications['text'] = 'One or more IPs are down!'
            notifications['fg'] = 'red'
            print("\n[Debug Error] One or more IPs are down!")
            print("[IPPing] Scan Process time = ", + time.process_time())
        else:
            notifications['text'] = 'All IPs are Up!'
            print("\n[Debug] Scan completed, all IP/Domains are up!")
            print("[IPPing] Scan Process time = ", + time.process_time())

        return self.progress.grid_forget(), self.ipopen.seek(0), self.ipopen.close(), \
               startfile("IPreport.txt"), print("[Debug] Below find the Ping responses per IP (0 = up / 1 = down"), \
               print(responses), self.after(4000, notifications.destroy)

    def newip(self):

        """
         This function adds a new IP/Domain to the IPlist.TXT file.
         Before anything it will check that the IP/Domain has 15 or less characters.
         Then newip will check if input_data is a str or number, if its a number ip
         it will proceed to check if self.validip is true as well as self.dupeip
         If input_data is a str newip will proceed to check that the str has a "." and
         that self.dupeip is true
         """
        #  This line open the default file and seeks it back to 0, very important!
        # ipopen = open("IPlist.txt")
        # ipopen.seek(0), ipopen.close()

        notifications = tk.Label(self, text="Thank you for using IPPing!", fg="green", font=("Arial Bold", 9))

        input_data = self.e1.get()

        if input_data == "":
            return print("[Debug] No input found!"), self.error()
        else:
            print("[Debug] Input Found... Proceeding")

        # This checks if IPlist.txt is empty or not
        if os.stat("IPlist.txt").st_size == 0:
            self.checkip()

            with open('IPlist.txt', mode='a') as add_ip:
                add_ip.seek(0)
                add_ip.write("{}\n".format(input_data))
                notifications['text'] = 'IP/Domain has been added!'
                notifications.grid(row=4, column=1)
                self.after(2000, notifications.destroy)
                add_ip.seek(0)
                print("[Debug] IP address {} has been added!".format(input_data))
            return print("[IPPing] New IP/Domain added!")
        else:
            print("[IPPing] IPlist.txt contains 1 or more IP's proceeding...")

        if len(input_data) > 15 or "":
            notifications['text'] = 'Please enter a valid IP/Domain'
            notifications['fg'] = 'red'
            notifications.grid(row=4, column=1)
            return print("[Debug Error] Input data has more than 15 characters!")
        else:
            print("[Debug] Input data is less than 15 characters, Passing onto next line")

        self.checkip()
        self.checkduplicate()

        try:
            input_data = int(input_data) or float(input_data)
            if self.validip and self.dupeip:
                with open('IPlist.txt', mode='a') as add_ip:
                    add_ip.seek(0)
                    add_ip.write("{}\n".format(input_data))
                    notifications['text'] = 'IP has been added!'
                    notifications.grid(row=4, column=1)
                    add_ip.seek(0)
                    print("[Debug] IP address {} has been added!".format(input_data))
            else:
                notifications['text'] = 'Invalid IPv4/IPv6 detected!'
                notifications.grid(row=5, column=1)
                print("[Debug Error] Is not valid IPv4/IPv6 or is duplicate on IPlist.txt")
            print("[Debug] User input is int ")  # This section detects integers and floats
        except ValueError:
            input_data = str(input_data)
            print("[Debug] User input is Str")  # This section detects the input as a str
            if "." in input_data and self.dupeip:
                with open('IPlist.txt', mode='a') as add_domain:
                    add_domain.seek(0)
                    add_domain.write("{}\n".format(input_data))
                    print("Domain {} has been added!".format(input_data))
                    notifications['text'] = 'IP/Domain has been added!'
                    notifications.grid(row=4, column=1)
                    add_domain.seek(0)
            else:
                notifications['text'] = 'Invalid IP or Duplicate found!'
                notifications['fg'] = 'red'
                notifications.grid(row=4, column=1)
                print("[Debug Error] Incorrect Domain entry or is duplicate!")

        return self.after(4000, notifications.destroy)

    def contents(self):

        """
        This function reads the IP/Domain on the IPlist.TXT file and outputs them
        It will also open IPreport.txt for the user to see all recent reports in one txt file.
        """
        notifications = tk.Label(self, text="Thank you for using IPPing!", fg="green", font=("Arial Bold", 9))

        print("[Debug] IPlist.txt has been opened!")
        ipopen = open("IPlist.txt")

        # Opens the IPlist.txt file and strips each of the lines so that we can read individually.
        with open("IPlist.txt", "r") as ips_file:
            ips = [ip.strip() for ip in ips_file.readlines()]

        with open("IPlist.txt", mode='r') as read:
            for ip in ips:
                print(ip)

        notifications['text'] = 'IPlist.txt has been opened!'
        notifications['fg'] = 'green'
        notifications.grid(row=5, column=1)

        return ipopen.seek(0), ipopen.close(), startfile("IPlist.txt"), self.after(2000, notifications.destroy)

    def clear_reports(self):
        """This function will clear the contents of reports, will also display labels
        and remove previous ones by triggering forget_labels function"""

        notifications = tk.Label(self, text="Recent reports cleared!", fg="green", font=("Arial Bold", 9))

        self.cls()
        ipreport = open("IPreport.txt", "w+")
        notifications['text'] = 'Recent reports have been cleared!'
        notifications['fg'] = 'green'
        notifications.grid(row=6, column=1)
        print("[Debug] Recent Reports have been cleared!")
        self.after(3000, notifications.destroy)

        return ipreport.close()  # startfile("IPreport.txt")

    """-------------------------------------Settings Section------------------------------------"""

    def Select_file(self):
        """
            Scans Root of App and Folder called UserData/Lists for previous saved IP Lists
            - dir_name = tk.filedialog.askdirectory() # This selects a folder directory
            - filedialog.asksaveasfilename(initialdir="/",
              title="Select file", filetypes=(("Txt File", "*.txt"),
              ("all files", "*.*"))) # This asks to save
        """

        l_newscanfile = tk.Label(self.win, text="IP Scan Directory\n" "Has Been Updated!", fg="green",
                                 font=("Arial Bold", 9))

        self.customscanfile = tk.filedialog.askopenfilename(initialdir="/", title="Select file",
                                                            filetypes=(("Txt Files", "*.txt"),
                                                                       ("all files", "*.*")))

        change = []
        self.lines = []
        change.append(self.customscanfile)

        if "" in change:
            print("[Debug] No change was made... exiting.")
            return
        else:
            settings = open("Settings.txt", "r")
            with open("Settings.txt", mode='r') as s:
                settinglines = [ip.strip() for ip in s.readlines()]
                print(settinglines)
                self.default_scan = False

            with open('Settings.txt', mode='a') as add:
                self.replace_line('Settings.txt', 0, "{}\n".format("DefaultScanFile=False"))
                add.write("{}\n".format(self.customscanfile))
                #  User GUI Notification
                l_newscanfile.grid(row=8, column=0)
                self.after(3000, l_newscanfile.destroy)
                print("[Debug] Scan File directory changed to:", self.customscanfile)

        return settings.close()

    def settingsdefault(self):

        """
            This function will simply set the Settings.txt file back to it's
            default format, overwritting the current Settings.txt
        """
        l_default = tk.Label(self.win, text="Settings Generated!", fg="green", font=("Arial Bold", 9))

        settings = open("Settings.txt", "w+")

        with open("Settings.txt", mode='w+') as s:
            s.write("DefaultScanFile=True\n")
            s.write("DefaultPackets=True\n")
            s.write("PacketsAmount=\n")
            s.write("1\n")
            s.write("DefaultScanDir=\n")

        return print("[IPPing] Settings have been reset to Default!"), l_default.grid(row=9, column=0), \
               self.after(3000, l_default.destroy)

    def customscandir(self):

        """This function is used to return the directory location of the user
           specified scan file, This is stored on the Settings.txt"""

        self.intdefaultscan()

        if self.default_scan:
            return "IPlist.txt"
        else:
            try:
                with open("Settings.txt", mode='r') as s:
                    settinglines = [ip.strip() for ip in s.readlines()]

                if " " in settinglines[5]:
                    return messagebox.showerror('IPPing', 'No directory has been found on Setting.txt\n' +
                                                "Reset the settings to default or select a scan file"), \
                           print("[Error] Nothing found on last line")

                else:
                    print("Using custom scan dir")
                    return settinglines[5]
            except FileNotFoundError:
                return messagebox.showerror('IPPing', 'No directory has been found on Setting.txt\n' +
                                            "Reset the settings to default or select a scan file"), \
                       print("[Error] Nothing found on last line")

    def custompackets(self):

        """This function is used to return the amount of packets specified by
           the user on settings, This is stored on the Settings.txt"""

        with open("Settings.txt", 'r') as s:
            settinglines = [ip.strip() for ip in s.readlines()]
            print(settinglines)

        if "DefaultPackets=True" in settinglines[1]:
            return int(1)
        else:
            return settinglines[3]

    def changepackets(self):

        """This function will handle changing the amount of packets that get sent per IP"""

        l_packets = tk.Label(self.pack, text="Packets amount updated\n" "on Settings.txt!", fg="green",
                             font=("Arial Bold", 9))

        if self.scale_pack.get() == 0:
            print("[Debug] Hey silly! Nothing has been changed, silly goose!")
        else:
            print("[Debug] User has selected a packet amount")
            settings = open("Settings.txt", "a")

            with open("Settings.txt", mode='r') as s:
                settinglines = [ip.strip() for ip in s.readlines()]
                print(settinglines)

            with open('Settings.txt', mode='a') as add:
                self.replace_line('Settings.txt', 1, "{}\n".format("DefaultPackets=False"))
                self.replace_line('Settings.txt', 3, "{}\n".format(self.scale_pack.get()))
                print("[Debug] DefaultPackets set to False", self.scale_pack.get())
                print("[Debug] Scan File directory changed to:", self.scale_pack.get())

        #  User GUI Notification
        l_packets.grid(row=7, column=0)
        self.after(2500, l_packets.destroy)

    """------------------------------------------Backend Code Functions----------------------------------------------"""

    def intdefaultfiles(self):

        try:
            ipreports = open("IPreport.txt")
            ipreports.close()
        except (FileNotFoundError, IndexError, IOError) as error:
            ipreports = open("IPreport.txt", "w+")
            ipreports.close()
            print("[Debug] intdefaultfile > Has generated IPreport.txt")

        try:
            iplist = open("IPlist.txt")
            iplist.close()

        except (FileNotFoundError, IndexError, IOError) as error:
            iplist = open("IPlist.txt", "w+")
            iplist.write("google.com")
            iplist.close()
            print("[Debug] intdefaultfile > Has generated IPlist.txt")

        try:
            settings = open("Settings.txt")
            settings.close()
        except (FileNotFoundError, IndexError, IOError) as error:
            with open("Settings.txt", 'w+') as s:
                s.write("DefaultScanFile=True\n")
                s.write("DefaultPackets=True\n")
                s.write("PacketsAmount=\n")
                s.write("1\n")
                s.write("DefaultScanDir=\n")
                s.close()
                print("[Debug] intdefaultfile > Has generated Settings.txt")

    def intdefaultscan(self):

        '''This function is triggered upon script startup, it checks if default
            scan directory is set to True or False on settings'''

        settings = open("Settings.txt")
        with open("Settings.txt", mode='r') as s:
            settinglines = [ip.strip() for ip in s.readlines()]

            if "DefaultScanFile=True" in settinglines[0]:
                self.default_scan = True
            else:
                self.default_scan = False

        return print("[IPPing] Has been set to {}".format(self.default_scan))

    def defaultscancheck(self):

        """This function checks if the Default Scan file is being used or a custom one"""

        try:
            if self.default_scan:
                try:
                    self.ipopen = open("IPlist.txt")
                    print("[Debug] Default Scan File detected")
                except FileNotFoundError:
                    print("[Debug] No default scan file was detected! Generating IPlist.txt...")
                    self.ipopen = open("IPlist.txt", "w+")
                    self.ipopen.write("google.com")
                    messagebox.showinfo('Notice', 'No IPlist.txt file was found,\n' +
                                        "So we generated one for you!")
            else:
                self.ipopen = open("{}".format(self.customscandir()))
                print("[Debug] Custom Scan File detected")
        except (FileNotFoundError, IndexError, IOError) as error:
            return self.error()

    def checkip(self):

        """This function will check the IP entered by the user, it will make sure
        that its a proper IPv4 or IPv6 IP address then return a True or False"""

        try:
            socket.inet_aton(self.e1.get())
            print("[Debug] validIP Set to True")
            self.validip = True
        except socket.error:
            print("[Debug] is Valid IPv4/IPv6 Set to False")
            self.validip = False

        return self.validip

    def checkduplicate(self):

        """This function checks for a duplicate IP or Domain on the IPlist.txt file
        then returns True or False"""

        notifications = tk.Label(self, text="Thank you for using IPPing!", fg="red", font=("Arial Bold", 9))

        ipopen = open("IPlist.txt", "r")

        with open("IPlist.txt", "r") as ip_file:
            ips = [ip.strip() for ip in ip_file.readlines()]

            for ip in ips:
                if self.e1.get() == ip:
                    self.dupeip = False
                    print("[Debug Error] Dup Found")
                    notifications['text'] = 'Duplicate IP/Domain detected!'
                    notifications.grid(row=5, column=1)
                    self.after(3000, notifications.destroy)
                    break
                else:
                    self.dupeip = True

            print("[Debug] Dup not found")

        return self.dupeip, ipopen.seek(0), ipopen.close()

    """----------------------------------------As back end code as you can get---------------------------------------"""

    def error(self):
        return messagebox.showerror('Error', 'Please enter an IP/domain')

    def replace_line(self, file_name, line_num, text):
        """self.replace_line('Settings.txt', 3, "{}\n".format(self.scale_pack.get()))"""
        lines = open(file_name, 'r').readlines()
        lines[line_num] = text
        out = open(file_name, 'w')
        out.writelines(lines)
        out.close()

    def timestamp(self, fname, fmt='%Y-%m-%d-%H-%M-%S_{fname}'):
        return datetime.datetime.now().strftime(fmt).format(fname=fname)

    def timestamp2(self, fmt='%Y-%m-%d-%H-%M-%S'):
        return datetime.datetime.now().strftime(fmt).format()

    def cls(self):
        # This is horrible way to handle this? Maybe, but it solves this problem for now. :)
        return print('\n' * 50)
        # os.system('cls' if os.name == 'nt' else 'clear')

    def close_window(self):
        self.destroy()

    def destroy_widget(widget):
        widget.destroy()
