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

        self.l_sep = tk.Label(self, text="___________").grid(row=1)
        self.iptxt = tk.Label(self, text="Enter IP:", font=("Arial Bold", 9)).grid(row=2)

        tk.Button(self, bg="green", text='Settings', command=self.settings).grid(row=0, sticky=tk.SW, column=1, pady=2),

        tk.Button(self, bg="green", text='Add New IP', command=self.newip).grid(row=0, column=0, pady=2),
        tk.Button(self, text='Open IPlist', command=self.contents).grid(row=0, column=1, sticky=tk.SE, pady=2),
        tk.Button(self, text='Clear Reports', command=self.reports).grid(row=0, column=3, sticky=tk.SE, pady=2),
        tk.Button(self, text='Ping All IPs', command=self.scanlist).grid(row=0, column=2, sticky=tk.SE, pady=2),
        tk.Button(self, text='Exit', command=self.quit).grid(row=0, column=4, pady=2)

        self.scanfile = ""
        self.default_scan = True

        self.validip = False
        self.dupeip = False

        self.e1 = tk.Entry(self, bg='grey', fg='white', font=("Arial Bold",))
        self.e1.grid(row=2, column=1)

    def settings(self):
        print("[IPPing] Settings GUI has been started")
        win = tk.Toplevel()
        win.wm_title("IPPing Settings")
        win.geometry("150x200+700+300")

        # Logo for settings GUI
        self.image2 = tk.PhotoImage(file="images\\settings.png")
        self.limage = tk.Label(win, image=self.image2)
        self.limage.grid()

        # Buttons for settings GUI
        l = tk.Label(win, text="Select File to Scan From")
        l.grid(row=1, column=0)
        b = tk.Button(win, text="Select file", command=self.Select_file)
        b.grid(row=2, column=0)

        default_button = tk.Button(win, text="Default Settings", command=self.settingsdefault)
        default_button.grid(row=5, column=0)

        # Notification labels for the settings GUI
        self.label_newscanfile = tk.Label(win, text="IP Scan Directory\n" "Has Been Changed", fg="green", font=("Arial Bold", 9))
        self.label_default = tk.Label(win, text="Settings Generated!", fg="green", font=("Arial Bold", 9))


class App(tk.Tk):
    """This class uses the Tkinter module and its used to call buttons labels change
    certain settings with in Tkinter module etc... onto the the GUI"""

    def __init__(self):
        super().__init__()
        print("[IPPing] GUI started!")
        print("- Author: Hontiris1")

        # self.grid()
        self.title("IPPing")
        self.geometry("450x155+900+300")

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
