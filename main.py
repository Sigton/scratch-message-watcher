'''
SCRATCH MESSAGE WATCHER
By Sigton

A simple GUI to give live updates on Scratch messages
'''

# This GUI is made using tkinter
import tkinter as tk
from tkinter import ttk

# JSON is used to turn the data retrieved from the API into Python data structures
import json, time

# Requests is used to get the data in the first place :P
try:
    import requests
except ImportError:
    raise ImportError

# Define the fonts
LARGE_FONT = ("Verdana", 12)

class MessageWatcherApp(tk.Tk):

    '''
    Main backend class, this is what makes stuff work.
    '''

    def __init__(self, *args, **kwargs):

        ''' Constructor '''
        
        # Call the parents constructor        
        tk.Tk.__init__(self, *args, **kwargs)

        # Set the window title
        tk.Tk.wm_title(self, "Scratch Message Watcher")

        # Create the container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        # And configure the grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Create a dictionary of frames and append all pages to it
        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        # Set the starting page
        self.show_frame(StartPage)

    def show_frame(self, cont):

        # Simple function to switch pages

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    '''
    This is all content on the starting page
    '''

    def __init__(self, parent, controller):

        ''' Constructor '''

        # Call the parents constructor
        tk.Frame.__init__(self,parent)

        # Added a label
        self.title = ttk.Label(self, text="Welcome to the Scratch Message Watcher", font=LARGE_FONT)
        self.title.pack(pady=10,padx=10)
        self.label = ttk.Label(self, text="You you have 0 new messages")
        self.label.pack()

    def update(self):

        # This is the main function; it retrieves the message count from the api and converts it from JSON to a Python dict.

        r = requests.get("https://api.scratch.mit.edu/proxy/users/Sigton/activity/count")
        d = json.loads(str(r.content)[2:-1])
        message_count = d['msg_count']

        self.label.config(text="You have {0} new messages".format(message_count))

        time.sleep(5)
        self.update()

def main():
    
    # Main function
    
    app = MessageWatcherApp()
    StartPage.update()
    app.mainloop()

if __name__ == '__main__':
    main()
