import tkinter as tk
from tkinter import ttk
import requests

class MessageWatcherApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

app = MessageWatcherApp()
app.mainloop()
