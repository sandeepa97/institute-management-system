from tkinter import *
import csv


with open ("profile.csv", "w") as db:
    writer = csv.writer(db)
    writer.writerow(["NAME ", "GENDER"]) # create with heading


def save_details():
    global e1               # global variable to receive the data from entry
    data = e1.get()
    Sex = option.get()   # this will get the value of radio selected and append it to the file
    totalinput = [ data, Sex] # Sex here to append to the csv file
    with open("profile.csv", "a") as savedb:
        w = csv.writer(savedb)
        w.writerow(totalinput)


def validate():
    value = option.get()  # this for radiobutton

    now = new.get()  # this for an entry widget

    if value != "male" and value != "female":
        print("An option must be selected")
    else:
        print(now)


root = Tk()
root.geometry("400x400")

new = StringVar()
e1 = Entry(root, textvariable=new)

option = StringVar()
R1 = Radiobutton(root, text="MALE", value="male", var=option, indicatoron=0)
R2 = Radiobutton(root, text="FEMALE", value="female", var=option, indicatoron=0)
button = Button(root, text="OK", command=lambda :[save_details(), validate()])


e1.pack()
R1.pack()
R2.pack()
button.pack(side="bottom")

root.mainloop()