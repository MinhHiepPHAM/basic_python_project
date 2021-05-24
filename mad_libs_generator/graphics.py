# See the package relative imports:
# https://docs.python.org/3/reference/import.html#package-relative-importsmport
import tkinter as tk
from tkinter import messagebox
from madlibs_def import *

def message_family():
    tk.messagebox.showinfo("My family", madlib_family())

def message_color():
    messagebox.showinfo("My favorite color", madlib_color())

def message_dream():
    messagebox.showinfo("My dream", madlib_dream())

root = tk.Tk()
root.geometry("300x200")
root.title("Mad libs generator")
tk.Button(root, text="family", command=message_family).place(x=50, y=50)
tk.Button(root, text="color", command=message_color).place(x=50, y=90)
tk.Button(root, text="dream", command=message_dream).place(x=50, y=130)
tk.Label(root, text="click one option:", font="arial 15 bold").place(x=50, y=10)
root.mainloop()

