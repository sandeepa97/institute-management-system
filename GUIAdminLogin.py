from tkinter import *

window = Tk()
window.title("Student Management System")

# Init setup
window.configure(background = "lemon chiffon")
window.minsize(width = 250, height = 120)

def click_Yes():
    print("Yes!")


# Components
title = Label(window, text = "Admin Login") 
title.config(font =("Courier", 14))

Label(window, text = "Username").grid(row = 5, column = 2, sticky = E)
Label(window, text = "Password").grid(row = 7, column = 2, sticky = E)

txtFullName = Entry(window, width = 20)
txtAddress = Entry(window, width = 20)

title.grid(row = 0, column = 3, sticky = E)
txtFullName.grid(row = 5, column = 3, sticky = E)
txtAddress.grid(row = 7, column = 3, sticky = E)


def readEntry():
    print(txtFullName.get())


Button(window, text = "Login", width = 12, bd = 4, command = readEntry, bg = "LightBlue1").grid(row = 20, column = 3, sticky = E)
Button(window, text = "Cancel", width = 12, bd = 4, command = readEntry, bg = "LightBlue1").grid(row = 20, column = 4, sticky = E)

window.mainloop()