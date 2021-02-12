from tkinter import *

window = Tk()
window.title("Student Management System")

# Init setup
window.configure(background = "lemon chiffon")
window.minsize(width = 550, height = 300)

def click_Yes():
    print("Yes!")


# Components
title = Label(window, text = "Student Registration") 
title.config(font =("Courier", 14))

Label(window, text = "First Name").grid(row = 5, column = 2, sticky = E)
Label(window, text = "Last Name").grid(row = 7, column = 2, sticky = E)
Label(window, text = "Gender").grid(row = 9, column = 2, sticky = E)
Label(window, text = "Date of Birth").grid(row = 11, column = 2, sticky = E)
Label(window, text = "NIC").grid(row = 13, column = 2, sticky = E)
Label(window, text = "Contact Number").grid(row = 15, column = 2, sticky = E)
Label(window, text = "Email").grid(row = 17, column = 2, sticky = E)
Label(window, text = "Address").grid(row = 19, column = 2, sticky = E)
Label(window, text = "Guardian Name").grid(row = 21, column = 2, sticky = E)
Label(window, text = "Guardian Contact").grid(row = 23, column = 2, sticky = E)

txtFirstName = Entry(window, width = 20)
txtLastName = Entry(window, width = 20)
txtGender = Entry(window, width = 20)
txtDOB = Entry(window, width = 20)
txtNIC = Entry(window, width = 20)
txtContact = Entry(window, width = 20)
txtEmail = Entry(window, width = 20)
txtAddress = Entry(window, width = 20)
txtGName = Entry(window, width = 20)
txtGContact = Entry(window, width = 20)

title.grid(row = 0, column = 3, sticky = E)

txtFirstName.grid(row = 5, column = 3, sticky = E)
txtLastName.grid(row = 7, column = 3, sticky = E)
Checkbutton(window, text="Male").grid(row = 9, column = 3, sticky = E)
Checkbutton(window, text="Female").grid(row = 9, column = 4, sticky = W)
txtDOB.grid(row = 11, column = 3, sticky = E)
txtNIC.grid(row = 13, column = 3, sticky = E)
txtContact.grid(row = 15, column = 3, sticky = E)
txtEmail.grid(row = 17, column = 3, sticky = E)
txtAddress.grid(row = 19, column = 3, sticky = E)
txtGName.grid(row = 21, column = 3, sticky = E)
txtGContact.grid(row = 23, column = 3, sticky = E)


def readEntry():
    print(txtFullName.get())

Button(window, text = "New", width = 12, bd = 4, command = readEntry, bg = "LightBlue1").grid(row = 25, column = 1, sticky = E)
Button(window, text = "Submit", width = 12, bd = 4, command = readEntry, bg = "LightBlue1").grid(row = 25, column = 3, sticky = E)
Button(window, text = "Cancel", width = 12, bd = 4, command = readEntry, bg = "LightBlue1").grid(row = 25, column = 4, sticky = E)


window.mainloop()