from tkinter import *
from tkinter import ttk,messagebox
import connection,login
class Student:
    def __init__(self):
        self.root = Tk()
        self.root.title("Student Managemenet system")
        self.root.geometry("1350x768+0+0")
        self.root.config(bg="black")

        title=Label(self.root,text='Student mangement system'.upper(),bd=10,relief=GROOVE,font=("times new roman",40,'bold'),bg="cyan",fg="red")
        title.pack(side=TOP,fill=X)

        color="blue2"
        #=========variables==================
        self.name_var = StringVar()
        self.roll_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.database = connection.Connection()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        #=========Manage frame===============
        manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg=color)
        manage_Frame.place(x=20,y=100,width=450,height=600)

        m_title = Label(manage_Frame,text="Manage Student",bg=color,fg="white",font=("times new roman",30,'bold'))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll = Label(manage_Frame,text="Roll No. ",bg=color,fg="white",font=("times new roman",20,'bold'))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky='w')
        txt_roll = Entry(manage_Frame,font=("times new roman",15,'bold'),textvariable=self.roll_var,bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=7,padx=20,sticky='w')

        lbl_name = Label(manage_Frame,text="Name ",bg=color,fg="white",font=("times new roman",20,'bold'))
        lbl_name.grid(row=2,column=0,pady=7,padx=20,sticky='w')
        txt_name = Entry(manage_Frame,font=("times new roman",15,'bold'),textvariable=self.name_var,bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=7,padx=20,sticky='w')

        lbl_Email = Label(manage_Frame,text="Email ",bg=color,fg="white",font=("times new roman",20,'bold'))
        lbl_Email.grid(row=3,column=0,pady=7,padx=20,sticky='w')
        txt_Email = Entry(manage_Frame,font=("times new roman",15,'bold'),textvariable=self.email_var,bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=7,padx=20,sticky='w')

        lbl_gender = Label(manage_Frame,text="Gender ",bg=color,fg="white",font=("times new roman",20,'bold'))
        lbl_gender.grid(row=4,column=0,pady=7,padx=20,sticky='w')
        combo_gender = ttk.Combobox(manage_Frame,font=("times new roman",15,'bold'),textvariable=self.gender_var,state="readonly")
        combo_gender['values']=("Male","Female","Other")
        self.gender_var.set("Select Gender")
        combo_gender.grid(row=4,column=1,pady=7,padx=20,sticky='w')
        
        lbl_contact = Label(manage_Frame,text="Contact ",bg=color,fg="white",font=("times new roman",20,'bold'))
        lbl_contact.grid(row=5,column=0,pady=7,padx=20,sticky='w')
        txt_contact = Entry(manage_Frame,font=("times new roman",15,'bold'),textvariable=self.contact_var,bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=7,padx=20,sticky='w')

        lbl_dob = Label(manage_Frame,text="D.O.B. ",bg=color,fg="white",font=("times new roman",20,'bold'))
        lbl_dob.grid(row=6,column=0,pady=7,padx=20,sticky='w')
        txt_dob = Entry(manage_Frame,font=("times new roman",15,'bold'),textvariable=self.dob_var,bd=5,relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=7,padx=20,sticky='w')

        lbl_address = Label(manage_Frame,text="Address ",bg=color,fg="white",font=("times new roman",20,'bold'))
        lbl_address.grid(row=7,column=0,pady=7,padx=20,sticky='w')
        self.text_address = Text(manage_Frame,width=20,height=4,font=("times new roman",15,'bold'),bd=3,relief=GROOVE)
        self.text_address.grid(row=7,column=1,pady=7,padx=20,sticky='w')

        #=========Button Frame=======
        btn_Frame =  Frame(manage_Frame,bd=4,relief=RIDGE,bg=color)
        btn_Frame.place(x=10,y=530,width=420)

        add_btn = Button(btn_Frame,text="Add",width=5,command=self.add_students).grid(row=0,column=0,padx=16,pady=10)
        update_btn = Button(btn_Frame,text="Update",width=5,command=self.update_data).grid(row=0,column=1,padx=16,pady=10)
        delete_btn = Button(btn_Frame,text="Delete",width=5,command=self.delete_data).grid(row=0,column=2,padx=16,pady=10)
        clear_btn = Button(btn_Frame,text="Clear",width=5,command=self.clear_fun).grid(row=0,column=3,padx=16,pady=10) 

        #=========Details Frame======
        details_Frame = Frame(self.root,bd=4,relief=RIDGE,bg=color)
        details_Frame.place(x=500,y=100,width=820,height=600)

        lbl_search = Label(details_Frame,text="Search By",bg=color,fg="white",font=("times new roman",20,'bold'))
        lbl_search.grid(row=0,column=0,pady=10,padx=15,sticky='w')
        
        combo_search = ttk.Combobox(details_Frame,width=12,textvariable=self.search_by,font=("times new roman",15,'bold'),state="readonly")
        combo_search['values']=("roll_no","name",'contact')
        self.search_by.set("Select Option")
        combo_search.grid(row=0,column=1,pady=10,padx=15,sticky='w')
        
        txt_search = Entry(details_Frame,textvariable=self.search_txt,font=("times new roman",10,'bold'),width=25,bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=15,sticky='w')
        
        search_btn = Button(details_Frame,text="Search",width=5,command=self.search_by_fun).grid(row=0,column=4,padx=10,pady=10)
        show_btn = Button(details_Frame,text="Show all",width=5,command=self.fatch_data).grid(row=0,column=5,padx=10,pady=10)
        logout_btn = Button(details_Frame,text="Logout",width=5,command=self.logout).grid(row=0,column=6,padx=10,pady=10)

        #==========Table Frame============
        table_Frame =  Frame(details_Frame,bd=4,relief=RIDGE,bg=color)
        table_Frame.place(x=10,y=70,width=790,height=510)

        scroll_x = Scrollbar(table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(table_Frame,orient=VERTICAL)
        self.Student_table = ttk.Treeview(table_Frame,columns=("roll","name","email","gender","contact", "dob", "address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll",text="Roll No.")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="D.O.B.")
        self.Student_table.heading("address",text="Address")
        self.Student_table['show'] = "headings"
        r_width = 85
        self.Student_table.column("roll",width=r_width)
        self.Student_table.column("name",width=r_width*2)
        self.Student_table.column("email",width=r_width*3)
        self.Student_table.column("gender",width=r_width)
        self.Student_table.column("contact",width=r_width*2)
        self.Student_table.column("dob",width=r_width*2)
        self.Student_table.column("address",width=r_width*3)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fatch_data()
        self.root.mainloop()

    def add_students(self):
        r=0
        try:
            if self.roll_var.get() != "":
                r=int(self.roll_var.get())
            else:
                messagebox.showerror("Error","Roll must be required")
        except:
            messagebox.showerror("Error","Roll should be integer")
        else:
            if r!=0:
                self.database.add_data(
                    r,
                    self.name_var.get(),
                    self.email_var.get(),
                    self.gender_var.get(),
                    self.contact_var.get(),
                    self.dob_var.get(),
                    self.text_address.get('1.0',END)
                )
                self.clear_fun()
        self.fatch_data()
        
    def clear_fun(self):
        self.name_var.set("")
        self.roll_var.set("")
        self.email_var.set("")
        self.gender_var.set("Select Gender")
        self.contact_var.set("")
        self.dob_var.set("")
        self.text_address.delete("1.0",END)
        self.search_by.set("Select Option")
        self.search_txt.set("")
        # self.Student_table.delete(*self.Student_table.get_children())
    
    def fatch_data(self):
        rows = self.database.fatch_all_data()
        self.Student_table.delete(*self.Student_table.get_children())
        if len(rows) != 0:
            for row in rows:
                self.Student_table.insert("",END,values=row)
                
    def get_cursor(self,ev):
        cursor_row = self.Student_table.focus()
        content = self.Student_table.item(cursor_row)
        rows = content['values']
        self.name_var.set(rows[1])
        self.roll_var.set(rows[0])
        self.email_var.set(rows[2])
        self.gender_var.set(rows[3])
        self.contact_var.set(rows[4])
        self.dob_var.set(rows[5])
        self.text_address.delete("1.0",END)
        self.text_address.insert(END,rows[6])

    def update_data(self):
        r=0
        try:
            if self.roll_var.get() != "":
                r=int(self.roll_var.get())
            else:
                messagebox.showerror("Error","Roll must be required")
        except:
            messagebox.showerror("Error","Roll should be integer")
        else:
            if r!=0:
                self.database.update_data(
                            r,
                            self.name_var.get(),
                            self.email_var.get(),
                            self.gender_var.get(),
                            self.contact_var.get(),
                            self.dob_var.get(),
                            self.text_address.get('1.0',END)
                        )
                self.clear_fun()
        self.fatch_data()

    def delete_data(self):
        r=0
        try:
            if self.roll_var.get() != "":
                r=int(self.roll_var.get())
            else:
                messagebox.showerror("Error","Roll must be required")
        except:
            messagebox.showerror("Error","Roll should be integer")
        else:
            if r!=0:
                self.database.delete_data(r)
                self.clear_fun()
        self.fatch_data()

    def search_by_fun(self):
        if self.search_by.get() == "" or self.search_txt.get() == "":
            messagebox.showerror("Error","Search bar is emety")
        else:
            try:
                temp = f"'{self.search_txt.get()}'"
                rw = self.database.search_by_database(self.search_by.get(),temp)
                self.Student_table.delete(*self.Student_table.get_children())
                if len(rw) != 0:
                    for row in rw:
                        self.Student_table.insert("",END,values=row)
            except:
                messagebox.showerror("Error","Not Found")
    def logout(self):
        self.root.destroy()
        login.Login()

