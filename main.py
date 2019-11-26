import ipfunc as ipfunc
import tkinter as tk


class GUIframeworkmain(ipfunc.IPfunctions):
    """This class communicates with ipfunc.py using the IPfunctions class"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.test = tk.Label(self, text="___________").grid(row=1)
        self.iptxt = tk.Label(self, text="Enter IP Address:").grid(row=2)

        tk.Button(self, text='Add New IP', command=self.newip).grid(row=0, column=0, pady=2),
        tk.Button(self, text='List of IPs', command=self.contents).grid(row=0, column=1, sticky=tk.SE,pady=2),
        tk.Button(self, text='Scan all IPs', command=self.scanlist).grid(row=0, column=2, sticky=tk.SE,pady=2),
        tk.Button(self, text='Quit', command=self.quit).grid(row=0, column=3, pady=2)

        self.e1 = tk.Entry(self)
        self.e1.grid(row=2, column=1)


class App(tk.Tk):
    """This class uses the Tkinter module and its used to call buttons labels change
    certain settings with in Tkinter module etc... onto the the GUI"""
    def __init__(self):
         super().__init__()

         self.title("IPPing")
         self.geometry("400x115+900+300")

         #calls the GUIframework class onto Tkinter GUI module
         self.ip_function = GUIframeworkmain(self)
         self.ip_function.grid()


if __name__ == '__main__':
    App().mainloop()
