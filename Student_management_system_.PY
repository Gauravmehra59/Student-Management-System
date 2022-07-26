from tkinter import*
from tkinter import ttk
import mysql.connector as c
import tkinter.messagebox as mssg
class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Managment System")
        self.root.geometry("2000x800+0+0") 
        p1 = PhotoImage(file=r"C:\Users\LENOVO\Downloads\image_search_1627963078887.png")

        self.root.iconphoto(False,p1)

        self.lab = Label(self.root,text="Student Management System",font=("times new roman",25,"bold"),bg="green",fg="white",relief=GROOVE,bd=10).pack(fill=X)
        
#--------------------manage frame-----------------------------------------
        self.manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="green").place(x=20,y=70,width=500,height=600)

        manage_title = Label(self.manage_Frame,text="Student Entry",fg="white",font=("times new roman",25,"bold"),bg="green").place(x=50,y=90)
        
        name = Label(self.manage_Frame,text="Name",fg="white",font=("times new roman",20,"bold"),bg="green").place(x=50,y=150)
        self.nameval = StringVar()
        name_entry = ttk.Entry(self.manage_Frame,textvariable=self.nameval,font=("times new roman",15,"bold")).place(x=200,y=150,height=30,width=300)


        rollno = Label(self.manage_Frame,text="Rollno.",fg="white",font=("times new roman",20,"bold"),bg="green").place(x=50,y=210)
        self.rollnoval = StringVar()
        rollno_entry = ttk.Entry(self.manage_Frame,textvariable=self.rollnoval,font=("times new roman",15,"bold")).place(x=200,y=210,height=30,width=300)

# --------------Branch interchange with Course-------------
        branch = Label(self.manage_Frame,text="Course",fg="white",font=("times new roman",20,"bold"),bg="green").place(x=50,y=270)
        self.branchval = ttk.Combobox(self.manage_Frame,state="readonly",font=("times new roman",15,"bold")) 
        self.branchval["values"]=("Select","B.tech","B.com","M.tech","B.Pharm")
        self.branchval.place(x=200,y=270,height=30,width=300)
        self.branchval.current(0)
        
        

        

# -----------Course inter change with Branch---------------
        course = Label(self.manage_Frame,text="Branch",fg="white",font=("times new roman",20,"bold"),bg="green").place(x=50,y=330)
        self.course = ttk.Combobox(self.manage_Frame,state="readonly",font=("times new roman",15,"bold")) 
        self.course["values"]=("Select","C.S.E","Mech.","Civil","Elec.","Others")
        self.course.place(x=200,y=330,height=30,width=300)
        self.course.current(0)
        
        

        phone = Label(self.manage_Frame,text="Phone No.",fg="white",font=("times new roman",20,"bold"),bg="green").place(x=50,y=390)
        self.phoneval = StringVar()
        phone_entry = ttk.Entry(self.manage_Frame,textvariable=self.phoneval,font=("times new roman",15,"bold")).place(x=200,y=390,height=30,width=300)


        email = Label(self.manage_Frame,text="Email",fg="white",font=("times new roman",20,"bold"),bg="green").place(x=50,y=450)
        self.emailval = StringVar()
        email_entry = ttk.Entry(self.manage_Frame,textvariable=self.emailval,font=("times new roman",15,"bold")).place(x=200,y=450,height=30,width=300)

        gender =Label(self.manage_Frame,text="Gender",fg="white",font=("times new roman",20,"bold"),bg="green")
        gender.place(x=50,y=510)
        # self.gender_val = StringVar()
        self.gender_val = ttk.Combobox(self.manage_Frame,state="readonly",font=("times new roman",15,"bold"))
        self.gender_val["values"]=("Select","M","F","Other")
        self.gender_val.place(x=200,y=510,height=30,width=300)
        self.gender_val.current(0)

# --------------------Buttons----------------------------------
        submit_button = Button(self.manage_Frame,text="Submit",command=self.submit_data,font=("times new roman",20,"bold")).place(x=50,y=570,height=50,width=100)
        update_button = Button(self.manage_Frame,command=self.update,text="Update",font=("times new roman",20,"bold")).place(x=150,y=570,height=50,width=100)
        clear_button = Button(self.manage_Frame,text="Clear",command=self.clear,font=("times new roman",20,"bold")).place(x=250,y=570,height=50,width=100)
        delete_button = Button(self.manage_Frame,command=self.delete,text="Delete",font=("times new roman",20,"bold")).place(x=350,y=570,height=50,width=100)

        # #-------------total student label-------------------------

        con = c.connect(host="localhost",user = "root",password="gauravmehra59930@",database="gaurav")
        curser = con.cursor()

        curser.execute("select count(RollNo) from student_managment")
        counting = curser.fetchone() 
        counts = list(counting)
        total_student = Label(self.manage_Frame,text=f"The Total Student is {counts[0]}",bg="green",fg="white",font=("times new roman",20,"bold"))
        total_student.place(x=50,y=620)
        con.close()


        
        
        details_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="green").place(x=550,y=70,width=800,height=600)
        search_by = Label(details_Frame,text="Search By",font=("times new roman",25,"bold"),bg="green",fg="white").place(x=580,y=90) 
        self.searchval = ttk.Combobox(details_Frame,state="readonly")
        self.searchval["values"]=("Select","RollNo","PhoneNo","Name","Branch","Gender","Course")
        self.searchval.current(0)
        self.searchval.place(x=750,y=100,height=25)


        self.searchentryval = StringVar()
        search_by_entry = ttk.Entry(details_Frame,textvariable=self.searchentryval).place(x=900,y=100,height=25)

        search_by_button = Button(details_Frame,text="Search",font=("times new roman",15,"bold"),command=self.search).place(x=1050,y=100,height=25)
        show_button = Button(details_Frame,text="Show All",font=("times new roman",15,"bold"),command=self.fetch_data).place(x=1130,y=100,height=25)

        delet_all = Button(details_Frame,text="Delete All",font=("times new roman",15,"bold"),command=self.delete_all).place(x=1230,y=100,height=25)


        # --------------Record Search Frame ---------------------------------
        reocord_frame = Frame(details_Frame,bd=4,relief=RIDGE,bg="white").place(x=570,y=150,width=750,height=500)


        self.scroll_x = Scrollbar(reocord_frame,orient=HORIZONTAL)
        self.scroll_y = Scrollbar(reocord_frame,orient=VERTICAL)
        self.student_table = ttk.Treeview(reocord_frame,columns=("Name","Rollno.","Email","Course","Gender","Branch","Phone Number"),xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
        self.scroll_x.place(x=570,y=650,width=750)
        self.scroll_y.place(x=1320,y=150,height=500)
        self.scroll_x.config(command=self.student_table.xview)
        self.scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Rollno.",text="Rollno.")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Phone Number",text="Phone Number")
        self.student_table.heading("Branch",text="Branch")
        self.student_table.heading("Email",text="Email")
        self.student_table['show']='headings'

        self.student_table.place(x=580,y=170,width=730,height=480)
        
        self.fetch_data()
        self.student_table.bind("<ButtonRelease-1>",self.fetch_data_entry)
        
    def submit_data(self):
        try:
            global counts
            con = c.connect(host="localhost",user = "root",password="gauravmehra59930@",database="gaurav")
            curser = con.cursor()
            name = self.nameval.get()
            rollno = self.rollnoval.get()
            email= self.emailval.get()
            Branch= self.branchval.get()
            gender = self.gender_val.get()
            Course = self.course.get()
            phone_number = self.phoneval.get()

            query = "insert into student_managment values ('{}','{}','{}','{}','{}','{}','{}')".format(name,rollno,email,Branch,gender,Course,phone_number)
            curser.execute(query)
            con.commit()
            self.fetch_data()
            con = c.connect(host="localhost",user="root",password="gauravmehra59930@",database="gaurav")
            cur = con.cursor()

        
            count = cur.execute("select count(RollNo) from student_managment")

            countsss = cur.fetchone()
            counts = list(countsss)
            total_student = Label(self.manage_Frame,text=f"The Total Student is {counts[0]}",bg="green",fg="white",font=("times new roman",20,"bold"))
            total_student.place(x=50,y=620)
            con.close()
            mssg.showinfo("Success",f"Successfully Submit and Total student is {counts[0]}")

        except Exception as ex:
             mssg.showerror("Error","The Rollno. already register")   
    
    def fetch_data(self):
             con = c.connect(host="localhost",user = "root",password="gauravmehra59930@",database="gaurav")
             curser = con.cursor()

             curser.execute("select * from student_managment")
             rows = curser.fetchall()
             

             if len(rows)!=0:
                     self.student_table.delete(*self.student_table.get_children())
                     for row in rows:
                             self.student_table.insert('',END,values=row)
                     con.commit()
             con.close()                             

    def clear(self):
            self.nameval.set('')
            self.rollnoval.set('')
            self.emailval.set('')
            self.branchval.current(0)
            self.gender_val.current(0)
            self.course.current(0)
            self.phoneval.set('')
            

    def fetch_data_entry(self,event):
            curosor_row = self.student_table.focus()
            contents = self.student_table.item(curosor_row)
            row = contents["values"]
        
            self.nameval.set(row[0])
            self.rollnoval.set(row[1])
            self.emailval.set(row[2])
            self.branchval.set(row[3])
            self.gender_val.set(row[4])   
             
            self.course.set(row[5])

            self.phoneval.set(row[6])
            
               

    def delete(self):
            con = c.connect(host="localhost",user="root",password="gauravmehra59930@",database="gaurav")
            curser = con.cursor()

           
            nam = self.rollnoval.get()
            querry2 = "DELETE FROM student_managment WHERE RollNo='%s'"%(nam) 
            curser.execute(querry2)
            x = self.student_table.selection()[0]
            self.student_table.delete(x)
            
            con.commit() 
            count = curser.execute("select count(RollNo) from student_managment")

            countsss = curser.fetchone()
            counts = list(countsss)
            total_student = Label(self.manage_Frame,text=f"The Total Student is {counts[0]}",bg="green",fg="white",font=("times new roman",20,"bold"))
            total_student.place(x=50,y=620)
            
            con.close()
        
            self.clear()

            mssg.showinfo("Delete","Delete Successfully")



    def update(self):
         
            
            con = c.connect(host="localhost",user = "root",password="gauravmehra59930@",database="gaurav")
            curser = con.cursor()
            
            name = self.nameval.get()
            rollno = self.rollnoval.get()
            email= self.emailval.get()
            Course= self.branchval.get()
            gender = self.gender_val.get()
            Branch = self.course.get()
            phone_number = self.phoneval.get()

        
        

            query = "UPDATE student_managment set Name='{}', RollNo='{}',Email = '{}' , Course = '{}' , Gender = '{}' , Branch = '{}' , PhoneNo = '{}'  WHERE  RollNo = '{}'".format(name,rollno,email,Course,gender,Branch,phone_number,rollno)
            curser.execute(query)
            con.commit()
            self.fetch_data()
            con.close()
            mssg.showinfo("Success","Successfully Update")    
        
        


    def delete_all(self):
            con = c.connect(host="localhost",user = "root",password="gauravmehra59930@",database="gaurav")
            curser = con.cursor()
            curser.execute("TRUNCATE TABLE student_managment")
            count = curser.execute("select count(RollNo) from student_managment")

            countsss = curser.fetchone()
            counts = list(countsss)
            total_student = Label(self.manage_Frame,text=f"The Total Student is {counts[0]}",bg="green",fg="white",font=("times new roman",20,"bold"))
            total_student.place(x=50,y=620)
            con.close()
            mssg.showinfo("Delete","Delete Successfully")
        
            for item in self.student_table.get_children():
                    self.student_table.delete(item)

            
        

    def search(self):
        
            con = c.connect(host="localhost",user = "root",password="gauravmehra59930@",database="gaurav")
            curser = con.cursor()
            curser.execute("SELECT * FROM student_managment WHERE "+str(self.searchval.get())+" LIKE '%"+str(self.searchentryval.get())+"%' ")
            rows = curser.fetchall()
            
             

            if len(rows)!=0:
                     self.student_table.delete(*self.student_table.get_children())
                     i=0
                     for row in rows:
                             self.student_table.insert('',END,values=row)
                             i=i+1
                     mssg.showinfo("Record",f"{i} Student Found")    
                     con.commit()
            
            con.close()    

            if rows == []:
                    mssg.showinfo("Search","No Record Found")                         
            
            

root=Tk()
od = Student(root)
root.mainloop()