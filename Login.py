from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector as mycon
class SignIn:
    def __init__(self,root):
        self.root=root
        self.root.title("EMERALD AIRLINES")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

        self.lbl=ImageTk.PhotoImage(file="images/b3.jpg")
        lbl=Label(self.root,image=self.lbl).place(x=0,y=0,relheight=1,relwidth=1)

        self.side=ImageTk.PhotoImage(file="images/side2.jpg")
        side=Label(self.root,image=self.side).place(x=225,y=100,width=300,height=500)

        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=525,y=100,width=600,height=500)

        title=Label(login_frame,text="SIGN IN",font=("calibri",30,"bold","underline"),bg="white",fg="blue").place(x=220,y=40)

        email=Label(login_frame,text="Email Address",font=("calibri",20,"bold"),bg="white",fg="gray").place(x=80,y=150)       
        self.txt_email=Entry(login_frame,font=("calibri",18),bg="lightgray")
        self.txt_email.place(x=80,y=200,width=440,height=35) 

        pass_=Label(login_frame,text="Password",font=("calibri",20,"bold"),bg="white",fg="gray").place(x=80,y=250)       
        self.txt_pass_=Entry(login_frame,font=("calibri",18),bg="lightgray")
        self.txt_pass_.place(x=80,y=300,width=440,height=35)

        btn_login=Button(login_frame,text="Sign In",command=self.signin,font=("calibri",20),bd=0,cursor="hand2",bg="coral",fg="black").place(x=220,y=380,width=160)

    def signin(self):
        if self.txt_email.get()=="" or self.txt_pass_.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                con=mycon.connect(host='localhost',user='root',password='password')
                cur=con.cursor()
                cur.execute("CREATE DATABASE IF NOT EXISTS FLIGHT")
                con.commit()
                cur.execute("USE FLIGHT")
                query="SELECT * FROM Employee WHERE EMAIL=%s AND PASSWORD=%s"
                values=(self.txt_email.get(),self.txt_pass_.get())
                cur.execute(query,values)
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Email And Password",parent=self.root)
                else:
                    messagebox.showinfo("Success","Welcome",parent=self.root)
                    self.root.destroy()
                    import main
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error Due To: {str(es)}",parent=self.root)
                
root=Tk()
obj=SignIn(root)
root.mainloop()
