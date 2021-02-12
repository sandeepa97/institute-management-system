from tkinter import *

window = Tk()
window.title("Student Management System")

# Init setup
window.configure(background = "lemon chiffon")
window.minsize(width = 500, height = 250)

def click_Yes():
    print("Yes!")


# Components
title = Label(window, text = "System Report Generation") 
title.config(font =("Courier", 14))

Label(window, text = "Report Type").grid(row = 9, column = 2, sticky = E)
Label(window, text = "Start Date").grid(row = 13, column = 2, sticky = E)
Label(window, text = "End Date").grid(row = 14, column = 2, sticky = E)
txtFirstName = Entry(window, width = 20)
txtGender = Entry(window, width = 20)
txtDOB = Entry(window, width = 20)
txtNIC = Entry(window, width = 20)


title.grid(row = 0, column = 3, sticky = E)

txtFirstName.grid(row = 5, column = 3, sticky = E)

Checkbutton(window, text="Student Reports").grid(row = 9, column = 3, sticky = E)
Checkbutton(window, text="Payments Reports").grid(row = 9, column = 4, sticky = W)
Checkbutton(window, text="Attendance Reports").grid(row = 10, column = 3, sticky = E)
Checkbutton(window, text="Classes Reports").grid(row = 10, column = 4, sticky = W)


txtDOB.grid(row = 13, column = 3, sticky = E)
txtNIC.grid(row = 14, column = 3, sticky = E)



def readEntry():
    print(txtFullName.get())

Button(window, text = "New", width = 12, bd = 4, command = readEntry, bg = "LightBlue1").grid(row = 25, column = 1, sticky = E)
Button(window, text = "Submit", width = 12, bd = 4, command = readEntry, bg = "LightBlue1").grid(row = 25, column = 3, sticky = E)
Button(window, text = "Cancel", width = 12, bd = 4, command = readEntry, bg = "LightBlue1").grid(row = 25, column = 4, sticky = E)


window.mainloop()