import sys
import os
from tkinter import *



def cancel():
    window.destroy()

def openStundentDetails():
    os.system('python GUIViewStudents.py')
def openPaymentDetails():
    os.system('python GUIViewPayments.py')
def openAttendanceDetails():
    os.system('python GUIViewAttendance.py')

def ReportsGUI():

    global window
    
    window = Tk()
    window.title("Student Management System")

    # Init setup
    window.configure(background = "lemon chiffon")
    window.minsize(width = 200, height = 225)


    # Components

    title = Label(window, text = "Reports") 
    title.config(font =("Courier", 14))

    title.grid(row = 0, column = 6, sticky = E)

    Button(window, text = "Student Reports", width = 15, bd = 4, command = openStundentDetails, bg = "LightBlue1").grid(row = 2, column = 6, sticky = E)
    Button(window, text = "Payments Reports", width = 15, bd = 4, command = openPaymentDetails, bg = "LightBlue1").grid(row = 3, column = 6, sticky = E)
    Button(window, text = "Attendance Reports", width = 15, bd = 4, command = openAttendanceDetails, bg = "LightBlue1").grid(row = 5, column = 6, sticky = E)

    Button(window, text = "Cancel", width = 12, bd = 4, command = cancel, bg = "LightBlue1").grid(row = 25, column = 7, sticky = E)

    window.mainloop()


ReportsGUI()
