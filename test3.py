from tkinter import *

root = Tk()

name_label = Label(root, text='Name')
name_entry = Entry(root)

gender_label = Label(root, text='Gender')
male = Radiobutton(root, text='Male')
female = Radiobutton(root, text='Female')

name_label.grid(row=1, column=1)
name_entry.grid(row=1, column=2, columnspan=2)

gender_label.grid(row=4, column=1)
male.grid(row=4, column=2, sticky="nsew")
female.grid(row=4, column=3, sticky="nsew")

root.mainloop()