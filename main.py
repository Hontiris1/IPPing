from ipfunc import *
import ipfunc as ipfunc
import tkinter as tk
from tkinter import *
from tkinter.ttk import *


class GUIframework(ipfunc.GUIframework):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.test = tk.Label(self, text="___________").grid(row=1)
        self.iptxt = tk.Label(self, text="Enter IP Address").grid(row=2)

        tk.Button(self, text='Add New IP', command=self.newip).grid(row=0, column=0, pady=2),
        tk.Button(self, text='List of IPs', command=self.contents).grid(row=0, column=1, sticky=tk.SE,pady=2),
        tk.Button(self, text='Scan all IPs', command=self.scanlist).grid(row=0, column=2, sticky=tk.SE,pady=2),
        tk.Button(self, text='Quit', command=self.quit).grid(row=0, column=3, pady=2)

        self.e1 = tk.Entry(self)
        self.e1.grid(row=2, column=1)


class Contents(ipfunc.GUIframework):
    def __init__(self, parent):
        super().__init__(parent)



class App(tk.Tk):
     def __init__(self):
         super().__init__()

         self.title("IPPing")
         self.geometry("340x130+900+300")

         self.ip_function = GUIframework(self)
         self.ip_function.grid()

if __name__ == '__main__':
    App().mainloop()
