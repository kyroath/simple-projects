"""

A simple calculator program

"""

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Simple Calculator")

mainframe = ttk.Frame(root, padding="3 3 3 3")
mainframe.grid(column=0, row=0, sticky="NWSE")



root.mainloop()