import os
from tkinter import *
from tkinter import messagebox
import csv

def cancel():
    window.destroy()
def openDashboard():
    os.system('python GUIDashboard.py')

def login():
    global user
    with open('admin.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        my_dict = [k:v for k,v in reader]
    user = txtUsername.get()
    password1 = txtPassword.get()
    if (my_dict[user]) == (password1):
        auth1 = True
        welcome1 = ("Welcome", user)
        messagebox.showinfo("Login info", welcome1)
        window.destroy()
        openDashboard()
    else:
        messagebox.showerror("Login error", "Incorrect username")

def LoginUI():

    global window
    global txtUsername
    global txtPassword
    global loginButton

    window = Tk()
    window.title("Student Management System")

    # Init setup
    window.configure(background = "lemon chiffon")
    window.minsize(width = 250, height = 120)


    # Components
    title = Label(window, text = "Admin Login") 
    title.config(font =("Courier", 14))

    Label(window, text = "Username").grid(row = 5, column = 2, sticky = E)
    Label(window, text = "Password").grid(row = 7, column = 2, sticky = E)

    txtUsername = Entry(window, width = 20)
    txtPassword = Entry(window, width = 20)

    title.grid(row = 0, column = 3, sticky = E)
    txtUsername.grid(row = 5, column = 3, sticky = E)
    txtPassword.grid(row = 7, column = 3, sticky = E)


    loginButton = Button(window, text = "Login", width = 12, bd = 4, command = login, bg = "LightBlue1").grid(row = 20, column = 3, sticky = E)
    Button(window, text = "Cancel", width = 12, bd = 4, command = cancel, bg = "LightBlue1").grid(row = 20, column = 4, sticky = E)

    window.mainloop()

LoginUI()