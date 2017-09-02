"""

The check-palindrome made again with a simple gui using tkinter

"""

from tkinter import *
from tkinter import ttk
from sys import exit

def checkIfPalindrome(*args):
    word = user_input.get()
    if word == word[::-1]:
        result.set("Palindrome!")
    else:
        result.set("Not")

root = Tk()
root.title("Check if Palindrome")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, S, E))

mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

user_input = StringVar()
result = StringVar()

word_entry = ttk.Entry(mainframe, width=10, textvariable=user_input)
word_entry.grid(column=1, row=1)

ttk.Label(mainframe, textvariable=result).grid(column=2, row=2)
ttk.Button(mainframe, text="Check!", command=checkIfPalindrome).grid(column=3, row=1)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

word_entry.focus()

root.bind("<Return>", checkIfPalindrome)
root.bind("<Escape>", exit)
root.mainloop()
