#!/usr/bin/env python
#############################################################
#   Author: Hontiris1                                       #
#   Github: https://github.com/Hontiris1/IPPing             #
#   Description: This script main purpose is to ping        #
#   - every IP on a txt file, and report data for each      #
#   - individual IP.                                        #
#############################################################
import ipfunc as ipfunc
import tkinter as tk


class GUIframeworkmain(ipfunc.IPfunctions):
    """This class communicates with ipfunc.py file using the IPfunctions class and objects"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Start a function to make changes to Settings.txt
        self.intdefaultfiles()
        self.intdefaultscan()

        self.l_sep = tk.Label(self, text="___________").grid(row=1)
        self.iptxt = tk.Label(self, text="Enter IP:", font=("Arial Bold", 9)).grid(row=2)

        tk.Button(self, bg="green", text='Settings', command=self.settings,relief="ridge").grid(row=0, sticky=tk.SW, column=1, pady=2),

        tk.Button(self, bg="green", text='Add New IP', command=self.newip, relief="ridge").grid(row=0, column=0, pady=2),
        tk.Button(self, text='Open IPlist', command=self.contents).grid(row=0, column=1, sticky=tk.SE, pady=2),
        tk.Button(self, text='Clear Reports', command=self.clear_reports).grid(row=0, column=3, sticky=tk.SE, pady=2),
        tk.Button(self, text='Ping All IPs', command=self.scanlist).grid(row=0, column=2, sticky=tk.SE, pady=2),
        tk.Button(self, text='Exit', command=self.quit).grid(row=0, column=4, pady=2)

        self.e1 = tk.Entry(self, bg='grey', fg='white', font=("Arial Bold",), justify='center')
        self.e1.grid(row=2, column=1)

    def settings(self):
        print("[IPPing] Settings GUI successfully open")

        self.win = tk.Toplevel()
        self.win.wm_title("IPPing Settings")
        self.win.resizable(False, False)
        self.win.iconbitmap('images\\logo.ico')

        window_height = 250
        window_width = 147

        screen_width = self.win.winfo_screenwidth()
        screen_height = self.win.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))

        self.win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        # Logo for settings GUI
        self.image2 = tk.PhotoImage(file="images\\settings.png")
        self.limage = tk.Label(self.win, image=self.image2)
        self.limage.grid(row=0, column=0)

        # Buttons for settings GUI
        a = tk.Label(self.win, text="Select File to Scan From", font=("Arial Bold", 8))
        a.grid(row=1, column=0)
        b = tk.Button(self.win, text="Select file", command=self.Select_file)
        b.grid(row=2, column=0)

        c = tk.Label(self.win, text="Packet Settings", font=("Arial Bold", 8))
        c.grid(row=4, column=0)
        d = tk.Button(self.win, text="Packets", command=self.packetsset)
        d.grid(row=5, column=0)

        default_button = tk.Button(self.win, text="Default Settings", command=self.settingsdefault)
        default_button.grid(row=6, column=0)

    def packetsset(self):
        print("[IPPing] Packet Settings GUI successfully open")

        self.pack = tk.Toplevel()
        self.pack.wm_title("IPPing Settings")
        self.pack.resizable(False, False)
        self.pack.iconbitmap('images\\logo.ico')

        window_height = 150
        window_width = 180

        screen_width = self.pack.winfo_screenwidth()
        screen_height = self.pack.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))

        self.pack.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        self.scale_pack = tk.Scale(self.pack, from_=0, to=10, orient=tk.HORIZONTAL, width=12)
        self.scale_pack.grid(row=4, column=0)

        l = tk.Label(self.pack, text="Change the amount of packets\n" "That are sent per IP Scan",
                     font=("Arial Bold", 8))
        l.grid(row=3, column=0)

        b = tk.Button(self.pack, text="Change Packet Amount", command=self.changepackets)
        b.grid(row=5, column=0)


class App(tk.Tk):
    """This class uses the Tkinter module and its used to call buttons labels change
    certain settings with in Tkinter module etc... onto the the GUI"""

    def __init__(self):
        super().__init__()
        print("[IPPing] GUI started!")
        print("- Author: Hontiris1")

        window_height = 160
        window_width = 465

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))

        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        self.title("IPPing")
        self.resizable(False, False)
        self.iconbitmap('images\\logo.ico')

        self.image1 = tk.PhotoImage(file="images\\bgg.png")
        self.label_for_image = tk.Label(self, image=self.image1)
        self.label_for_image.grid()

        # calls the GUIframework class onto Tkinter GUI module
        print("[IPPing] GUI Buttons and txt entry added!")
        self.ip_function = GUIframeworkmain(self)
        self.ip_function.grid()


if __name__ == '__main__':
    """this runs the App class which is using the Tkinter module"""
    App().mainloop()
    App.iconbitmap("images\\logo.ico")