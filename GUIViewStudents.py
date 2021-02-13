import os
from tkinter import *
import csv


def cancel():
    window.destroy()

def studentDetails():

    global window
   
    window = Tk()
    window.title("Student Management System")

    # Init setup
    window.configure(background = "lemon chiffon")
    window.minsize(width = 550, height = 300)


    # Components

    title = Label(window, text = "Student Details") 
    title.config(font =("Courier", 14))
    title.grid(row = 0, column = 3, sticky = E)

    with open("studentsTable.csv", newline = "") as file:
        reader = csv.reader(file)

        r = 1
        for col in reader:
            c = 0
            for row in col:
                table = Label(window, width = 10, height = 2, text = row, relief = RIDGE)
                table.grid(row = r, column = c)
                c += 1
            r += 1


    Button(window, text = "Cancel", width = 12, bd = 4, command = cancel, bg = "LightBlue1").grid(row = 25, column = 20, sticky = E)

    window.mainloop()


studentDetails()
