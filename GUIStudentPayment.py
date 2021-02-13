import os
from tkinter import *
from tkinter import messagebox
import csv


def new():
    txtNIC.delete(0,'end')
    txtPaymentType.delete(0,'end')
    txtAmount.delete(0,'end')
    txtDate.delete(0,'end')


def cancel():
    window.destroy()

def writeToFile():
    with open('paymentsTable.csv', 'a') as f:
        w=csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow([txtNIC.get(),txtPaymentType.get(),txtAmount.get(),txtDate.get()])
    messagebox.showinfo("System", "Payment Added Successfully!")
    new() 
    

def studentPaymentGUI():

    global window
    global txtNIC
    global txtPaymentType
    global txtAmount
    global txtDate
    
    window = Tk()
    window.title("Student Management System")

    # Init setup
    window.configure(background = "lemon chiffon")
    window.minsize(width = 500, height = 200)


    # Components

    title = Label(window, text = "Student Payments") 
    title.config(font =("Courier", 14))

    Label(window, text = "Student NIC").grid(row = 5, column = 2, sticky = E)
    Label(window, text = "Payment Type").grid(row = 6, column = 2, sticky = E)
    Label(window, text = "Amount").grid(row = 11, column = 2, sticky = E)
    Label(window, text = "Date").grid(row = 13, column = 2, sticky = E)


    txtNIC = Entry(window, width = 20)
    txtPaymentType = Entry(window, width = 20)
    txtAmount = Entry(window, width = 20)
    txtDate = Entry(window, width = 20)


    title.grid(row = 0, column = 3, sticky = E)

    txtNIC.grid(row = 5, column = 3, sticky = E)
    txtPaymentType.grid(row = 6, column = 3, sticky = E)

    # Checkbutton(window, text="Registration Fee").grid(row = 9, column = 3, sticky = E)
    # Checkbutton(window, text="Monthly Fee").grid(row = 9, column = 4, sticky = W)
    txtAmount.grid(row = 11, column = 3, sticky = E)
    txtDate.grid(row = 13, column = 3, sticky = E)

    Button(window, text = "New", width = 12, bd = 4, command = new, bg = "LightBlue1").grid(row = 25, column = 1, sticky = E)
    Button(window, text = "Submit", width = 12, bd = 4, command=writeToFile, bg = "LightBlue1").grid(row = 25, column = 3, sticky = E)
    Button(window, text = "Cancel", width = 12, bd = 4, command = cancel, bg = "LightBlue1").grid(row = 25, column = 4, sticky = E)

    window.mainloop()


studentPaymentGUI()
