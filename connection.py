import pymysql, generator 
from tkinter import messagebox

class Connection:
    def __init__(self):
        try:
            self.con = pymysql.connect(host="localhost",user="root",password="root",database="stm")
            self.cur = self.con.cursor()
        except:
            messagebox.showerror("Error","Database connection Error!!!!")
        
    def add_data(self,roll,name,email,gender,contact,dob,address):
        try:
            self.cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(roll,name,email,gender,contact,dob,address))
            # self.cur.execute(f"insert into students values({roll},{name},{email},{gender},{contact},{dob},{address})")
            self.con.commit()
            messagebox.showinfo("Success","Data has been saved!!!") 
        except pymysql.err.IntegrityError as dup:
            messagebox.showerror("Error","Duplicate roll no!!!!")
            messagebox.showerror("Error","Data not saved!!!!")
        except :
            messagebox.showerror("Error","Data not saved!!!!")

    def _add_genaret_data(self):
        no_data = 100
        self.cur.execute("truncate table students")
        data_gen = generator.Genarator()
        roll_list = data_gen.roll_gen(no_data)
        name_list = data_gen.name_gen(no_data)
        email_list = data_gen.email_gen(no_data)
        gender_list = data_gen.gender_gen(no_data)
        contect_list = data_gen.contect_gen(no_data)
        dob_list = data_gen.dob_gen(no_data)
        address_list = data_gen.address_gen(no_data)
        for i in range(no_data):
            self.cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(int(roll_list[i]),name_list[i],email_list[i],gender_list[i],contect_list[i],dob_list[i],address_list[i]))
            self.con.commit()
        self.con.close()
    
    def query_fun(self,query):
        return self.cur.execute(query)
    
    def fatch_all_data(self):
        self.query_fun("select * from students")
        return self.cur.fetchall()
    
    def update_data(self,roll,name,email,gender,contact,dob,address):
        try:
            self.cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(name,email,gender,contact,dob,address,roll))
            self.con.commit()
            messagebox.showinfo("Success","Data has been Updated!!!")
        except :
            messagebox.showerror("Error","Data not Updated!!!!")
    
    def delete_data(self,roll):
        try:
            self.cur.execute("delete from students where roll_no=%s",roll)
            self.con.commit()
            messagebox.showinfo("Success","Data has been Deleted!!!")
        except :
            messagebox.showerror("Error","Data not Deleted!!!!")
    
    def search_by_database(self,by_lbl,by_value):
        try:
            self.cur.execute("select * from students where "+by_lbl+"="+ str(by_value))
            return self.cur.fetchall()
        except :
            messagebox.showerror("Error","Serching problem!!")


if __name__ == "__main__":
    ob=Connection()
    # ob._add_genaret_data()
    ob.search_by_database('contact','8498513607')