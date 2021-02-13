import os
from tkinter import *
from tkinter import messagebox
import csv


def new():
    txtNIC.delete(0,'end')
    txtClass.delete(0,'end')
    txtDate.delete(0,'end')
    txtTime.delete(0,'end')


def cancel():
    window.destroy()

def writeToFile():
    with open('attendanceTable.csv', 'a') as f:
        w=csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow([txtNIC.get(),txtClass.get(),txtDate.get(),txtTime.get()])
    messagebox.showinfo("showinfo", "Attendance Marked Successfully!")
    new() 
    

def studentAttendanceGUI():

    global window
    global txtNIC
    global txtClass
    global txtDate
    global txtTime
    
    window = Tk()
    window.title("Student Management System")

    # Init setup
    window.configure(background = "lemon chiffon")
    window.minsize(width = 500, height = 200)


    # Components

    title = Label(window, text = "Student Attendance") 
    title.config(font =("Courier", 14))

    Label(window, text = "Student NIC").grid(row = 5, column = 2, sticky = E)
    Label(window, text = "Class").grid(row = 9, column = 2, sticky = E)
    Label(window, text = "Date").grid(row = 13, column = 2, sticky = E)
    Label(window, text = "Time").grid(row = 14, column = 2, sticky = E)

    txtNIC = Entry(window, width = 20)
    txtClass = Entry(window, width = 20)
    txtDate = Entry(window, width = 20)
    txtTime = Entry(window, width = 20)
    title.grid(row = 0, column = 3, sticky = E)

    txtNIC.grid(row = 5, column = 3, sticky = E)
    txtClass.grid(row = 9, column = 3, sticky = E)
    # Checkbutton(window, text="2021 Physics Theory").grid(row = 9, column = 3, sticky = E)
    # Checkbutton(window, text="2021 ICT Revision").grid(row = 9, column = 4, sticky = W)
    # Checkbutton(window, text="2021 Physics Theory").grid(row = 10, column = 3, sticky = E)
    # Checkbutton(window, text="2021 ICT Revision").grid(row = 10, column = 4, sticky = W)
    # Checkbutton(window, text="2021 Physics Theory").grid(row = 11, column = 3, sticky = E)
    # Checkbutton(window, text="2021 ICT Revision").grid(row = 11, column = 4, sticky = W)
    # Checkbutton(window, text="2021 Physics Theory").grid(row = 12, column = 3, sticky = E)
    # Checkbutton(window, text="2021 ICT Revision").grid(row = 12, column = 4, sticky = W)
    txtDate.grid(row = 13, column = 3, sticky = E)
    txtTime.grid(row = 14, column = 3, sticky = E)

    Button(window, text = "New", width = 12, bd = 4, command = new, bg = "LightBlue1").grid(row = 25, column = 1, sticky = E)
    Button(window, text = "Submit", width = 12, bd = 4, command=writeToFile, bg = "LightBlue1").grid(row = 25, column = 3, sticky = E)
    Button(window, text = "Cancel", width = 12, bd = 4, command = cancel, bg = "LightBlue1").grid(row = 25, column = 4, sticky = E)

    window.mainloop()


studentAttendanceGUI()
