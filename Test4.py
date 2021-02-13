import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.geometry("180x90")
name1 = ["Mike", "Harry", "Siti", "Jenn"]

def loadstates():
    f = open("test.txt", "r")
    list_a = []
    list_a = f.readlines()
    f.close()
    return [int(i) for i in list_a] # Make sure your values are integers, not strings

def createCheckboxes():
    for value, y in zip(st, name1):
        x = tk.IntVar() # This is a tkinter variable. BooleanVar() will also work here
        x.set(value) # When modifying values of a tkinter variable, always use .set()
        check = ttk.Checkbutton(root, text=y, variable=x)
        check.var = x # Link the variable to the checkbutton so it isn't thrown out by garbage collection
        check.pack(anchor=tk.W)

st = loadstates()
createCheckboxes()
root.mainloop()