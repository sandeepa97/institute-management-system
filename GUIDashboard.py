import os
from tkinter import *



def cancel():
    window.destroy()

def openStundentRegister():
    os.system('python GUIStudentRegistration.py')
def openStundentDetails():
    os.system('python GUIViewStudents.py')
def openStundentPayment():
    os.system('python GUIStudentPayment.py')
def openPaymentDetails():
    os.system('python GUIViewPayments.py')
def openStundentAttendance():
    os.system('python GUIStudentAttendance.py')
def openAttendanceDetails():
    os.system('python GUIViewAttendance.py')
def openReports():
    os.system('python GUIReports.py')

def systemDashboardGUI():

    global window
    
    window = Tk()
    window.title("Student Management System")

    # Init setup
    window.configure(background = "lemon chiffon")
    window.minsize(width = 400, height = 225)


    # Components

    title = Label(window, text = "System Dashboard") 
    title.config(font =("Courier", 14))

    title.grid(row = 0, column = 5, sticky = E)

    Button(window, text = "Student Registration", width = 15, bd = 4, command = openStundentRegister, bg = "LightBlue1").grid(row = 2, column = 4, sticky = E)
    Button(window, text = "View Students", width = 15, bd = 4, command = openStundentDetails, bg = "LightBlue1").grid(row = 3, column = 4, sticky = E)
    Button(window, text = "Delete Students", width = 15, bd = 4, command = cancel, bg = "LightBlue1").grid(row = 4, column = 4, sticky = E)
    Button(window, text = "Mark Payment", width = 15, bd = 4, command = openStundentPayment, bg = "LightBlue1").grid(row = 2, column = 6, sticky = E)
    Button(window, text = "View Payments", width = 15, bd = 4, command = openPaymentDetails, bg = "LightBlue1").grid(row = 3, column = 6, sticky = E)
    Button(window, text = "Mark Attendance", width = 15, bd = 4, command = openStundentAttendance, bg = "LightBlue1").grid(row = 4, column = 6, sticky = E)
    Button(window, text = "View Attendance", width = 15, bd = 4, command = openAttendanceDetails, bg = "LightBlue1").grid(row = 5, column = 6, sticky = E)
    Button(window, text = "Reports", width = 15, bd = 4, command = openReports, bg = "LightBlue1").grid(row = 6, column = 6, sticky = E)
    Button(window, text = "EXIT", width = 15, bd = 4, command = cancel, bg = "red").grid(row = 10, column = 6, sticky = E)

    window.mainloop()


systemDashboardGUI()
