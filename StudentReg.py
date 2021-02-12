from tkinter import * 
import csv

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.output()

    def output(self):
        Label(text='Student ID:').pack(row=1,side=LEFT,padx=5,pady=5)
        self.e = Entry(root, width=10)
        self.e.pack(side=LEFT,padx=5,pady=5)
        Label(text='First Name:').pack(row=2,side=LEFT,padx=5,pady=5)
        self.e = Entry(root, width=10)
        self.e.pack(side=LEFT,padx=5,pady=5)
        Label(text='Last Name:').pack(row=3,side=LEFT,padx=5,pady=5)
        self.e = Entry(root, width=10)
        self.e.pack(side=LEFT,padx=5,pady=5)


        self.b = Button(root, text='Submit', command=self.writeToFile)
        self.b.pack(side=RIGHT,padx=5,pady=5)

    def writeToFile(self):
        with open('studentsTable.csv', 'a') as f:
            w=csv.writer(f, quoting=csv.QUOTE_ALL)
            w.writerow([self.e.get()])

if __name__ == "__main__":
    root=Tk()
    root.title('Student Management System')
    root.geometry('1000x100')
    app=App(master=root)
    app.mainloop()
    root.mainloop()