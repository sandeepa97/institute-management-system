import os
from tkinter import *
from tkinter import messagebox
import csv


def new():
    txtFirstName.delete(0,'end')
    txtLastName.delete(0,'end')
    txtDOB.delete(0,'end')
    txtNIC.delete(0,'end')
    txtContact.delete(0,'end')
    txtEmail.delete(0,'end')
    txtAddress.delete(0,'end') 
    txtGName.delete(0,'end')
    txtGContact.delete(0,'end')

def cancel():
    window.destroy()

def writeToFile():
    with open('studentsTable.csv', 'a') as f:
        w=csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow([txtFirstName.get(),txtLastName.get(),Male,Female,txtDOB.get(),txtNIC.get(),txtContact.get(),
        txtEmail.get(),txtAddress.get(),txtGName.get(),txtGContact.get()])
    messagebox.showinfo("showinfo", "Student Registered Successfully!")
    new() 
    

def studentRegistrationGUI():

    global window
    global txtFirstName
    global txtLastName
    global Male
    global Female
    global txtDOB
    global txtNIC
    global txtContact 
    global txtEmail
    global txtAddress 
    global txtGName
    global txtGContact
    
    window = Tk()
    window.title("Student Management System")

    # Init setup
    window.configure(background = "lemon chiffon")
    window.minsize(width = 550, height = 300)


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
    # txtGender = Entry(window, width = 20)
    Male = Checkbutton(window, text="Male")
    Female = Checkbutton(window, text="Female")
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
    Male.grid(row = 9, column = 3, sticky = E)
    Female.grid(row = 9, column = 4, sticky = W)
    txtDOB.grid(row = 11, column = 3, sticky = E)
    txtNIC.grid(row = 13, column = 3, sticky = E)
    txtContact.grid(row = 15, column = 3, sticky = E)
    txtEmail.grid(row = 17, column = 3, sticky = E)
    txtAddress.grid(row = 19, column = 3, sticky = E)
    txtGName.grid(row = 21, column = 3, sticky = E)
    txtGContact.grid(row = 23, column = 3, sticky = E)

    Button(window, text = "New", width = 12, bd = 4, command = new, bg = "LightBlue1").grid(row = 25, column = 1, sticky = E)
    Button(window, text = "Submit", width = 12, bd = 4, command=writeToFile, bg = "LightBlue1").grid(row = 25, column = 3, sticky = E)
    Button(window, text = "Cancel", width = 12, bd = 4, command = cancel, bg = "LightBlue1").grid(row = 25, column = 4, sticky = E)

    window.mainloop()


studentRegistrationGUI()
