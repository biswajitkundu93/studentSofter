from tkinter import *
from tkinter import messagebox
import student

class Login:
    def __init__(self):
        #creating windonw
        self.root = Tk()
        self.root.title("Billing Software")
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg='black')

        #veriable for taking input
        self.user = StringVar()
        self.password = StringVar()

        #creating frame for login page
        F1 = Frame(self.root, bd=10,bg="olive",relief=GROOVE)
        F1.place(x=450, y=150, height=350)

        #tile of the system
        title = Label(F1, text="Login system",bg="olive",fg="white", font=("times new roman", 30,"bold")).grid(row=0,columnspan=2,pady=20)

       #for taking imput from user

        #for username 
        labelusrname = Label(F1, text="Username :-",bg="olive",fg="white", font=("times new roman", 20,"bold")).grid(row=1, column=0, pady=10, padx=10) 
        txtuser = Entry(F1,bd=7, relief=GROOVE, width=25, font="arial 15 bold", textvariable=self.user).grid(row=1,column=1,padx=10,pady=10)

        #for password
        labelpassword = Label(F1, text="Password :-",bg="olive",fg="white", font=("times new roman", 20,"bold")).grid(row=2, column=0, pady=10, padx=10) 
        txtpassword = Entry(F1,bd=7, relief=GROOVE,show="*", width=25, font="arial 15 bold", textvariable=self.password).grid(row=2,column=1,padx=10,pady=10)

        #button 
        btnlog = Button(F1, text="Login", bd=7, width=10,bg="indigo",fg="white",font="arial 15 bold", command=self.log_fun).place(x=10, y=250)
        btnreset = Button(F1, text="Reset", bd=7, width=10,bg="indigo",fg="white",font="arial 15 bold",command=self.reset_fun).place(x=170, y=250)
        btnexit = Button(F1, text="Exit", bd=7, width=10,bg="indigo",fg="white",font="arial 15 bold",command=self.exit_fun).place(x=325, y=250)
        self.root.mainloop()
    

    def log_fun(self):
        uname = "Biswajit"
        password = "12345"
        if self.user.get() == uname and self.password.get() == password:
            self.root.destroy()
            student.Student()
            # messagebox.showinfo("Info",f"welcome {self.user.get()}!!! \n your password is {self.password.get()}")
        else:
            messagebox.showerror("Error", "invalid username or password")
    
    
    def reset_fun(self):
        self.user.set("")
        self.password.set("")

    
    def exit_fun(self):
        option = messagebox.askyesno("Exit", "Do you really want to exit...!!! ")
        if option > 0:
            self.root.destroy()
        else:
            return



