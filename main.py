'''
SCRATCH MESSAGE WATCHER
By Sigton

A simple GUI to give live updates on Scratch messages
'''

import tkinter as tk
from tkinter import ttk

import json

try:
    import requests
except ImportError:
    pass

LARGE_FONT = ("Verdana", 12)

class MessageWatcherApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Scratch Message Watcher")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for f in (StartPage, PageOne):

            frame = f(container, self)

            self.frames[f] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self,parent)

        label = ttk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Proceed to page 1",
                             command=lambda: controller.show_frame(PageOne))
        button1.pack()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self,parent)

        label = ttk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Start Page",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Get message count", command=get_message_count)
        button2.pack()

def update():

    r = requests.get("https://api.scratch.mit.edu/proxy/users/Sigton/activity/count")
    d = json.loads(str(r.content)[2:-1])
    
    message_count = d['msg_count']

def main():
    app = MessageWatcherApp()
    app.mainloop()

if __name__ == '__main__':
    main()
