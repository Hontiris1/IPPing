#############################################################
#   Author: Hontiris1                                       #
#   Github: https://github.com/Hontiris1/IPPing             #
#   Description: This script main purpose is to ping        #
#   - every IP on a txt file, and report data for each      #
#   - individual IP.                                        #
#############################################################
from fileinput import filename
import ipfunc as ipfunc
import tkinter as tk
from threading import Thread
import time


class GUIframeworkmain(ipfunc.IPfunctions):
    """This class communicates with ipfunc.py file using the IPfunctions class and objects"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.l_sep = tk.Label(self, text="___________").grid(row=1)
        self.iptxt = tk.Label(self, text="Enter IP:", font=("Arial Bold", 9)).grid(row=2)

        tk.Button(self, bg="green", text='Add New IP', command=self.newip).grid(row=0, column=0, pady=2),
        tk.Button(self, text='Open IPlist', command=self.contents).grid(row=0, column=1, sticky=tk.SE, pady=2),
        tk.Button(self, text='Clear Reports', command=self.reports).grid(row=0, column=2, sticky=tk.SE, pady=2),
        tk.Button(self, text='Ping All IPs', command=self.scanlist).grid(row=0, column=3, sticky=tk.SE, pady=2),
        tk.Button(self, text='Exit', command=self.quit).grid(row=0, column=4, pady=2)

        self.validip = False
        self.dupeip = False
        self.response = ""

        print("[Debug] Main Thread has been started")
        self.manager = ThreadManager()
        self.manager.start(1)


        self.e1 = tk.Entry(self, bg='grey', fg='white', font=("Arial Bold",))
        self.e1.grid(row=2, column=1)

class App(tk.Tk):
    """This class uses the Tkinter module and its used to call buttons labels change
    certain settings with in Tkinter module etc... onto the the GUI"""

    def __init__(self):
        super().__init__()

        self.title("IPPing")
        self.geometry("450x155+900+300")

        self.image1 = tk.PhotoImage(file="images\\bgg.png")
        self.label_for_image = tk.Label(self, image=self.image1)
        self.label_for_image.grid()

        # calls the GUIframework class onto Tkinter GUI module
        self.ip_function = GUIframeworkmain(self)
        self.ip_function.grid()


class ThreadManager:
    """Multi Threading manager"""
    def __init__(self):
        pass

    def start(self, threads):
        thread_refs = []
        for i in range(threads):
            t = MyThread(i)  # Thread(args=(1,))  # target=test(),
            t.daemon = True
            print('starting thread %i' % i)
            t.start()
        for t in thread_refs:
            t.join()


class MyThread(Thread):
    """Multi Threading"""
    def __init__(self, i):
        Thread.__init__(self)
        self.i = i

    def run(self):
        while True:
            print('hello from thread # {}'.format(self.i))
            time.sleep(.25)
            break


if __name__ == '__main__':
    """this runs the App class which is using the Tkinter module"""
    App().mainloop()
