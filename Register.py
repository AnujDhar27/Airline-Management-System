from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector as mycon
name=''
class SignUp:
    def __init__(self,root):
        self.root=root
        self.root.title("EMERALD AIRLINES")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        self.bg=ImageTk.PhotoImage(file="images/b2.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        self.left=ImageTk.PhotoImage(file="images/side.jpg")
        left=Label(self.root,image=self.left).place(x=125,y=100,width=400,height=500)

        frame1=Frame(self.root,bg="white")
        frame1.place(x=525,y=100,width=700,height=500)

        title=Label(frame1,text="SIGN UP",font=("calibri",25,"bold","underline"),bg="white",fg="blue").place(x=270,y=30)

        f_name=Label(frame1,text="Name",font=("calibri(body)",14,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("calibri",14),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)
        
        u_name=Label(frame1,text="User Name",font=("calibri(body)",14,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_uname=Entry(frame1,font=("calibri",14),bg="lightgray")
        self.txt_uname.place(x=370,y=130,width=250)
        
        contact=Label(frame1,text="Contact No.",font=("calibri(body)",14,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("calibri",14),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame1,text="Email",font=("calibri(body)",14,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("calibri",14),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)
        
        question=Label(frame1,text="Security Question",font=("calibri(body)",14,"bold"),bg="white",fg="gray").place(x=50,y=240)
        self.cmb_question=ttk.Combobox(frame1,font=("calibri",13),state='readonly',justify=CENTER)
        self.cmb_question['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.cmb_question.place(x=50,y=270,width=250)
        self.cmb_question.current(0)
        
        answer=Label(frame1,text="Answer",font=("calibri(body)",14,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("calibri",14),bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)
        
        password=Label(frame1,text="Password",font=("calibri(body)",14,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("calibri",14),show="*",bg="lightgray")
        self.txt_password.place(x=50,y=340,width=250)
        
        cpassword=Label(frame1,text="Confirm Password",font=("calibri(body)",14,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("calibri",14),show="*",bg="lightgray")
        self.txt_cpassword.place(x=370,y=340,width=250)

        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("calibri",12)).place(x=50,y=380)

        self.btn_img=ImageTk.PhotoImage(file="images/register.png")
        btn=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",bg="white",command=self.SignUp_data).place(x=250,y=410)

        btn_login=Button(self.root,text="Sign In",command=self.login_window,font=("calibri",15),bd=0,cursor="hand2",bg="coral").place(x=250,y=520,width=160)

        name=self.txt_fname.get()
    def login_window(self):
        self.root.destroy()
        import Login

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_uname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.cmb_question.current(0)

    def SignUp_data(self):
        if self.txt_fname.get()=="" or self.txt_email.get()=="" or self.txt_contact.get()=="" or self.cmb_question.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All Field Are Required",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Password And Confirm Password Should Be Same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree To Our Terms And Conditions",parent=self.root)
        else:
            try:
                con=mycon.connect(host='localhost',user='root',password='password')
                cur=con.cursor()
                cur.execute("CREATE DATABASE IF NOT EXISTS FLIGHT")
                con.commit()
                cur.execute("USE FLIGHT")
                cur.execute("CREATE TABLE IF NOT EXISTS Employee(NAME VARCHAR(50) ,USERNAME VARCHAR(50),CONTACT VARCHAR(11),EMAIL VARCHAR(50),SECURITY VARCHAR(50),ANSWER VARCHAR(50),PASSWORD VARCHAR(10) PRIMARY KEY)")
                con.commit()
                query="SELECT * FROM Employee WHERE EMAIL='{}'".format(self.txt_email.get())
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User Already Exists, Please Try With Another Email",parent=self.root)
                else:
                    query="INSERT INTO Employee(NAME,USERNAME,CONTACT,EMAIL,SECURITY,ANSWER,PASSWORD) VALUES(%s,%s,%s,%s,%s,%s,%s)"
                    values=(self.txt_fname.get(),self.txt_uname.get(),self.txt_contact.get(),self.txt_email.get(),self.cmb_question.get(),self.txt_answer.get(),self.txt_password.get())
                    cur.execute(query,values)
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","SignUp Successful",parent=self.root)
                    self.clear()
            except Exception as es:
                messagebox.showerror("Error",f"Error Due To: {str(es)}",parent=self.root)

root=Tk()
obj=SignUp(root)
root.mainloop()
