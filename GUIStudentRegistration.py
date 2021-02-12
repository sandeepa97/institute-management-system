from tkinter import *
import csv
# Define global variables
student_fields = ['ID', 'firstName', 'lastName', 'gender', 'dob', 'nic', 'contact', 'email', 'address', 'guardianName', 'guardianContact']
student_database = 'students.csv'


def display_menu():
    print("--------------------------------------")
    print(" Welcome to Student Management System")
    print("---------------------------------------")
    print("1. Add New Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Quit")


def add_student():
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    global student_fields
    global student_database

    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)

    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Data saved successfully")
    input("Press any key to continue")
    return




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

# def enterData():
option = StringVar()

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
R1 = Radiobutton(window, text="MALE", value="male", var=option, indicatoron=0)
R2 = Radiobutton(window, text="FEMALE", value="female", var=option, indicatoron=0)
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
# Male = Checkbutton(window, text="Male").grid(row = 9, column = 3, sticky = E)
# Female = Checkbutton(window, text="Female").grid(row = 9, column = 4, sticky = W)
txtDOB.grid(row = 11, column = 3, sticky = E)
txtNIC.grid(row = 13, column = 3, sticky = E)
txtContact.grid(row = 15, column = 3, sticky = E)
txtEmail.grid(row = 17, column = 3, sticky = E)
txtAddress.grid(row = 19, column = 3, sticky = E)
txtGName.grid(row = 21, column = 3, sticky = E)
txtGContact.grid(row = 23, column = 3, sticky = E)


def writeToFile():
    # print(txtFirstName.get())
    with open('studentsTable.csv', 'a') as f:
        w=csv.writer(f, quoting=csv.QUOTE_ALL)
        Gender = option.get()
        w.writerow([txtFirstName.get(),txtLastName.get(),Gender])

Button(window, text = "New", width = 12, bd = 4, command = writeToFile, bg = "LightBlue1").grid(row = 25, column = 1, sticky = E)
Button(window, text = "Submit", width = 12, bd = 4, command=writeToFile, bg = "LightBlue1").grid(row = 25, column = 3, sticky = E)
Button(window, text = "Cancel", width = 12, bd = 4, command = writeToFile, bg = "LightBlue1").grid(row = 25, column = 4, sticky = E)


window.mainloop()