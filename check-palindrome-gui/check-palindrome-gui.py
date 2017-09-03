"""

The check-palindrome made again with a simple gui using tkinter

"""

from tkinter import *
from tkinter import ttk
from sys import exit
from os import startfile


def checkIfPalindrome(*args):
    word = user_input.get()

    if word == '':
        result.set("Not Palindrome!")
        return

    file_name = open("checked.txt", "a+")
    file_name.seek(0)

    for words in file_name:
        words = ''.join(words.split())

        if word == words:
            result.set("Palindrome!")
            file_name.close()
            return

    if word == word[::-1]:
        result.set("Palindrome!")
        file_name.write(word + "\n")
    else:
        result.set("Not Palindrome")
    file_name.close()


def openTXT():
    filepath = "checked.txt"
    startfile(filepath)


root = Tk()
root.title("Check if Palindrome")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky="NWSE")

mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

user_input = StringVar(value='')
result = StringVar(value="You can use ENTER!")

word_entry = ttk.Entry(mainframe, width=20, textvariable=user_input)
word_entry.grid(column=0, row=0)

check_label = ttk.Button(mainframe, text="CHECK!", command=checkIfPalindrome)
check_label.grid(column=2, row=0, columnspan=3, sticky="EW")

see_results = ttk.Button(mainframe, text="See Previous Results", command=openTXT)
see_results.grid(column=2, row=1, columnspan=3, ipadx=5, ipady=5, sticky="EW")

word_result = ttk.Label(mainframe, textvariable=result, text="You can also press ENTER!")
word_result.grid(column=0, row=1, columnspan=1, sticky="EW")

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

word_entry.focus()

root.bind("<Return>", checkIfPalindrome)
root.bind("<Escape>", exit)

root.mainloop()
