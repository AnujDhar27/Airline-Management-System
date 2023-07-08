from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import mysql.connector as mycon
from tkinter import messagebox 
from tkinter import filedialog
from datetime import date
import random
import pickle

isclicked=False
Total=0
total=0
seats=0
p1=0
p2=0
p3=0
p4=0
p5=0
p6=0
yes=False
record=[]
c=[]
YES=False
class FLIGHT:
    def __init__(self,root):
        self.root=root
        self.root.title("EMERALD AIRLINES")
        

        con=mycon.connect(host='localhost',user='root',password='password')
        cur=con.cursor()

        cur.execute("CREATE DATABASE IF NOT EXISTS FLIGHT")
        con.commit()
        cur.execute("USE FLIGHT")
        cur.execute("CREATE TABLE IF NOT EXISTS DETAILS(ORIGIN VARCHAR(50),DESTINATION VARCHAR(50))")
        con.commit()
        values=[('KOLKATA','MUMBAI'),('KOLKATA','DELHI'),('MUMBAI','DELHI'),('DELHI','MUMBAI'),('DELHI','KOLKATA'),('MUMBAI','KOLKATA'),('k','m'),
                ('CHENNAI','MUMBAI'),('MUMBAI','CHENNAI'),('DELHI','CHENNAI'),('KOLKATA','CHENNAI'),('CHENNAI','KOLKATA'),
                ('BANGALORE','MUMBAI'),('MUMBAI','BANGALORE'),('BANGALORE','CHENNAI'),('CHENNAI','BANGALORE'),('DELHI','BANGALORE'),
                ('BANGALORE','DELHI'),('KOLKATA','BANGALORE'),('BANGALORE','KOLKATA')]
        for i in range(0,len(values)):
            query="INSERT INTO DETAILS (ORIGIN,DESTINATION) VALUES (%s,%s)"
            cur.execute(query,values[i])
            con.commit()

        numb=random.randint(101,999)
        fnum="FL"+str(numb)

        self.class_combo1=StringVar()

        Mainframe=Frame(self.root,bd=20,width=700,height=700,relief=RIDGE,bg="#aedb9f")
        Mainframe.grid()

        def clickme(btn):
            btn.configure(bg='#008000')
            global isclicked
            if btn==self.button2:
                self.return_label.config(state='disabled')
                self.return_entry.config(state='disabled')
                self.return_button.config(state='disabled')
                isclicked=True

        self.label=Label(Mainframe,text="EMERALD AIRLINES",font=("Helvetica",22),bg="#aedb9f")
        self.label.grid(row=0,column=0,columnspan=2)

        self.button1=Button(Mainframe,text="ROUND TRIP",font=("Helvetica",18),width=15,command=lambda :clickme(self.button1),bg="#00FFFF")
        self.button1.grid(row=1,column=0,padx=20,pady=10)

        self.button2=Button(Mainframe,text="ONEWAY TRIP",font=("Helvetica",18),width=15,command=lambda :clickme(self.button2),bg="#00FFFF")
        self.button2.grid(row=1,column=1,padx=20,pady=10)

        self.origin_label=Label(Mainframe,text="ORIGIN",font=("Helvetica",18),bg="#aedb9f")
        self.origin_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        self.destination_label=Label(Mainframe,text="DESTINATION",font=("Helvetica",18),bg="#aedb9f")
        self.destination_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        self.depart_label=Label(Mainframe,text="DEPART",font=("Helvetica",18),bg="#aedb9f")
        self.depart_label.grid(row=4,column=0,padx=5,pady=5,sticky=W)

        self.return_label=Label(Mainframe,text="RETURN",font=("Helvetica",18),bg="#aedb9f")
        self.return_label.grid(row=5,column=0,padx=5,pady=5,sticky=W)

        self.passangers_label=Label(Mainframe,text="PASSANGERS",font=("Helvetica",18),bg="#aedb9f")
        self.passangers_label.grid(row=6,column=0,padx=5,pady=5,sticky=W)

        self.adult_label= Label(Mainframe, text="ADULT",font=("Helvetica",12),bg="#aedb9f")
        self.adult_label.grid(row=6,column=0,padx=5,pady=5,sticky=E)

        self.child_label=Label(Mainframe,text="CHILD",font=("Helvetica",12),bg="#aedb9f")
        self.child_label.grid(row=7,column=0,padx=5,pady=5,sticky=E)

        self.class_label=Label(Mainframe,text='CLASS',font=("Helvetica",18),bg="#aedb9f")
        self.class_label.grid(row=8,column=0,padx=5,pady=5,sticky=W)

        self.white_label=Label(Mainframe,text=' ',font=("Helvetica",22),bg="#aedb9f")
        self.white_label.grid(row=9,column=0,padx=5,pady=5,sticky=W)

        #entry

        self.origin_entry=Entry(Mainframe,width=28)
        self.origin_entry.grid(row=2,column=1,columnspan=3,padx=5,pady=5)

        self.destination_entry=Entry(Mainframe,width=28)
        self.destination_entry.grid(row=3,column=1,columnspan=3,padx=5,pady=5)

        self.depart_entry=Entry(Mainframe,width=28)
        self.depart_entry.grid(row=4,column=1,columnspan=3,padx=5,pady=5)

        def get_date(bt):
            def cal_done():
                top.withdraw()
                root.quit()
            top = Toplevel(root)
            cal = Calendar(top,font="Arial 14", selectmode='day',cursor="arrow")
            cal.pack(fill="both", expand=True)
            ttk.Button(top, text="ok", command=cal_done).pack()
            selected_date = None
            root.mainloop()
            if bt==self.depart_button:
                self.depart_entry.insert(0,cal.selection_get())
            if bt==self.return_button:
                self.return_entry.insert(0,cal.selection_get())

        self.depart_button=Button(Mainframe,text="⬆",command=lambda :get_date(self.depart_button),bg="#00FFFF")
        self.depart_button.grid(row=4,column=2)

        self.return_entry=Entry(Mainframe,width=28)
        self.return_entry.grid(row=5,column=1,columnspan=3,padx=5,pady=5)

        self.return_button=Button(Mainframe,text="⬆",command=lambda :get_date(self.return_button),bg="#00FFFF")
        self.return_button.grid(row=5,column=2)

        self.adult_entry=Entry(Mainframe)
        self.adult_entry.grid(row=6,column=1)
        self.adult_entry.insert(0,'0')

        self.child_entry=Entry(Mainframe)
        self.child_entry.grid(row=7,column=1)
        self.child_entry.insert(0,'0')

        self.class_combo=ttk.Combobox(Mainframe,textvariable=self.class_combo1,state='readonly',
                          width=20)
        self.class_combo["value"]=('','ECONOMY','PREMIUM ECONOMY','BUISNESS')
        self.class_combo.current(0)
        self.class_combo.grid(row=8,column=1)

        #variable is stored in the root object
        self.root.counter = 0

        def clicked0():
            self.root.counter += 1
            self.adult_entry.delete(0,END)
            self.adult_entry.insert(0,root.counter)
        def clicked1():
            self.root.counter -=1
            self.adult_entry.delete(0,END)
            self.adult_entry.insert(0,root.counter)
        def click0():
            self.root.counter += 1
            self.child_entry.delete(0,END)
            self.child_entry.insert(0,root.counter)
        def click1():
            self.root.counter -= 1
            self.child_entry.delete(0,END)
            self.child_entry.insert(0,root.counter)
                
        self.adult0 = Button(Mainframe, text="+", command=clicked0,bg="#00FFFF")
        self.adult0.grid(row=6,column=2,padx=5,pady=5,sticky=W)

        self.adult1=Button(Mainframe, text="-", command=clicked1,bg="#00FFFF")
        self.adult1.grid(row=6,column=1,padx=5,pady=5,sticky=W)

        self.child0=Button(Mainframe, text="+", command=click0,bg="#00FFFF")
        self.child0.grid(row=7,column=2,padx=5,pady=5,sticky=W)

        self.child0=Button(Mainframe, text="-", command=click1,bg="#00FFFF")
        self.child0.grid(row=7,column=1,padx=5,pady=5,sticky=W)
        def bill_area():
            if YES==False:
                self.root4.withdraw()
            if YES==True:
                self.root5.withdraw()
            global Total
            self.root6=Tk()
            self.root6.title("EMERALD AIRLINES")
            T1 = Text(self.root6, height=30, width=70,font=("Helvetica",16))
            T1.grid(row=0,column=0,rowspan=10)
            T1.insert(END,"======================================================================\n")
            T1.insert(END,"                                                          EMERALD AIRLINES \n")
            T1.insert(END,"                                                      CONTACT NO: 033-9787899 \n")
            T1.insert(END,"                                                      MAIL-ID: emeraldairlines@gmail.com\n")
            T1.insert(END, f"                                                          DATE: {date.today()}\n")
            T1.insert(END," \n")
            T1.insert(END," \n")
            T1.insert(END," \n")
            T1.insert(END,"======================================================================\n")
            T1.insert(END," \n")
            T1.insert(END,f"   FLIGHT NO :\t\t\t\t{fnum}")
            T1.insert(END," \n")
            T1.insert(END,f"   ORIGIN :\t\t\t\t{self.origin_entry.get().upper()}\n")
            T1.insert(END,f"   DESTINATION :\t\t\t\t{self.destination_entry.get().upper()}\n")
            T1.insert(END,f"   DEPARTURE :\t\t\t\t{self.depart_entry.get()}\n")
            T1.insert(END,f"   PASSANGERS :\t\t\t\tADULT  :   {self.adult_entry.get()}\n")
            T1.insert(END,f"               \t\t\t\tCHILD  :   {self.child_entry.get()}\n")
            T1.insert(END,f"   CLASS :\t\t\t\t{self.class_combo1.get()}\n")
            T1.insert(END," \n")
            T1.insert(END,"======================================================================\n")
            con=mycon.connect(host='localhost',user='root',password='password')
            cur=con.cursor()
            cur.execute("USE FLIGHT")
            query="SELECT NAME,AADHAR_NO,AGE,GENDER FROM FLIGHTS,PASSANGERS WHERE  FLIGHTS.FLIGHT_NO=PASSANGERS.FLIGHT_NO AND FLIGHTS.FLIGHT_NO='{}'".format(fnum)
            cur.execute(query)
            T1.insert(END,"   NAME\t\t\tAADHAR NO\t\t\tAGE\tGENDER\n")
            result=cur.fetchall()
            for row in result:
            	T1.insert(END,f"   {row[0].upper()}\t\t\t{row[1]}\t\t\t{row[2]}\t{row[3].upper()}\n")
            T1.insert(END,"======================================================================\n")
            T1.insert(END," \n")
            T1.insert(END,"   SEAT NO.")
            for i in c:
            	T1.insert(END,f"\t\t\t\t\t\t\t{i}\n")
            T1.insert(END," \n")
            T1.insert(END,"======================================================================\n")
            T1.insert(END,"   CONTENTS\t\t\tPRICE\tQUANTITY\t\tTOTAL \n")
            T1.insert(END,"======================================================================\n")
            T1.insert(END,f"   Flight Tickets\t\t\tRs.{total}\t{int(self.child_entry.get())+int(self.adult_entry.get())}\t\tRs.{total * (int(self.child_entry.get())+int(self.adult_entry.get()))}\n")
            if yes==True:
                f=open('food.dat','rb')
                s=pickle.load(f)
                for i in s:
                    name=i[0]
                    p=i[1]
                    q=i[2]
                    tot=i[3]
                    T1.insert(END,f"   {name}\t\t\tRs.{p}\t{q}\t\tRs.{tot}\n")
            T1.insert(END," \n")
            T1.insert(END," \n")
            T1.insert(END," \n")
            T1.insert(END," \n")
            T1.insert(END,"======================================================================\n")
            Total=Total+total
            Total=Total+((12/100)*Total)
            T1.insert(END,"\t\t\t\t\t\t\tSGST :"    "6%\n")
            T1.insert(END,"\t\t\t\t\t\t\tCGST :"    "6%\n")
            T1.insert(END,f"\t\t\t\t\t  AMOUNT PAYABLE : {Total}\n")
            T1.insert(END," \n")
            T1.insert(END,"   NOTE :\n")
            T1.insert(END,"   1.You must wear all pieces of protective gear, such as masks and gloves before entering the airport terminal. Do not open your face masks at any time during the journey\n")
            T1.insert(END,"   2.Reach the airport at least two hours before the scheduled departure of your flight.Due to the additional guidelines, check-in and boarding can take longer.\n")
            T1.insert(END,"   3.All passengers must submit a self-declaration form regarding  their health, along with their Aarogya Setu app health data to certify themselves as being fit to fly.\n")
            T1.insert(END,"   4.Passengers will self-scan their boarding pass to limit contact with airport staff member.\n")
            T1.config(state='disabled')
            def save():
            	text_file=filedialog.asksaveasfilename(defaultextension=".*",title="Save File",filetypes=(("HTML Files","*.html"),("Text Files","*.txt"),("All Files","*.*")))
            	if text_file:
            		name=text_file
            		name=name.replace("","")
            		self.root6.title(f'{name} - "Ticket"')

            		text_file=open(text_file,'w')
            		text_file.write(T1.get(1.0,END))
            		text_file.close()
            		messagebox.showinfo("Success",'Thank you for chosing EMERALD AIRLINES')
            		self.root6.mainloop()
            	else:
            		messagebox.showerror("Error",f"Error Due To: {str(es)}",parent=self.root6)
            def exittt():
                self.root6.destroy()
                exit()
            save=Button(self.root6,text="SAVE",command=save)
            save.grid(row=11,column=0)
            exitt=Button(self.root6,text="EXIT",command=exittt).place(x=480,y=724)
            #exitt.grid(row=11,column=1,sticky=W)
            self.root6.mainloop()
        def submit_d():
            self.root3.withdraw()
            self.root4=Tk()
            self.root4.title("EMERALD AIRLINES")
            
            def Yes():
                self.root4.withdraw()
                global yes
                global YES
                YES=True
                yes=True
                self.root5=Tk()
                self.root5.title("EMERALD AIRLINES")
                
                Frame2=Frame(self.root5,bd=20,width=1200,height=1200,relief=RIDGE,bg="#aedb9f")
                Frame2.grid()             
                ll0=Label(Frame2,text="EMERALD AIRLINES MENU",font=("Arial bold",16),bg="#aedb9f")
                ll0.grid(row=0,column=0)
                
                ll00=Label(Frame2,text="YOUR ORDER",font=("Arial bold",10),bg="#aedb9f")
                ll00.grid(row=2,column=5,padx=50)
                
                ll1=Label(Frame2,text="Choco Chip Cookie",fg='green',bg="#aedb9f")
                ll1.grid(row=2,column=1,sticky=W)
                ll11=Label(Frame2,text="₹150",bg="#aedb9f")
                ll11.grid(row=2,column=2)
                bb1=Button(Frame2,text="Choose",command=lambda :click(bb1),bg="#00FFFF")
                bb1.grid(row=2,column=4,padx=30)
                combo =ttk.Combobox(Frame2)
                combo['values']= (0,1,2,3,4,5)
                combo.current(0) #set the selected item
                combo.grid(column=3, row=2,padx=30)

                ll2=Label(Frame2,text="Cashew(salted)",fg='green',bg="#aedb9f")
                ll2.grid(row=3,column=1,sticky=W)
                ll22=Label(Frame2,text="₹200",bg="#aedb9f")
                ll22.grid(row=3,column=2)
                bb2=Button(Frame2,text="Choose",command=lambda :click(bb2),bg="#00FFFF")
                bb2.grid(row=3,column=4,padx=30)
                combo2 =ttk.Combobox(Frame2)
                combo2['values']= (0,1,2,3,4,5)
                combo2.current(0) #set the selected item
                combo2.grid(column=3, row=3,padx=30)

                ll3=Label(Frame2,text="Veg Mayo Sandwich",fg='green',bg="#aedb9f")
                ll3.grid(row=4,column=1,sticky=W)
                ll33=Label(Frame2,text="₹350",bg="#aedb9f")
                ll33.grid(row=4,column=2)
                bb3=Button(Frame2,text="Choose",command=lambda :click(bb3),bg="#00FFFF")
                bb3.grid(row=4,column=4,padx=30)
                combo3 =ttk.Combobox(Frame2)
                combo3['values']= (0,1,2,3,4,5)
                combo3.current(0) #set the selected item
                combo3.grid(column=3, row=4,padx=30)

                ll4=Label(Frame2,text="Paneer Tikka Sandwich",fg='green',bg="#aedb9f")
                ll4.grid(row=5,column=1,sticky=W)
                ll44=Label(Frame2,text="₹375",bg="#aedb9f")
                ll44.grid(row=5,column=2)
                bb4=Button(Frame2,text="Choose",command=lambda :click(bb4),bg="#00FFFF")
                bb4.grid(row=5,column=4,padx=30)
                combo4 =ttk.Combobox(Frame2)
                combo4['values']= (0,1,2,3,4,5)
                combo4.current(0) #set the selected item
                combo4.grid(column=3, row=5,padx=30)

                ll5=Label(Frame2,text="Chicken Tikka Sandwich",fg='red',bg="#aedb9f")
                ll5.grid(row=6,column=1,sticky=W)
                ll55=Label(Frame2,text="₹400",bg="#aedb9f")
                ll55.grid(row=6,column=2)
                bb5=Button(Frame2,text="Choose",command=lambda :click(bb5),bg="#00FFFF")
                bb5.grid(row=6,column=4,padx=30)
                combo5 =ttk.Combobox(Frame2)
                combo5['values']= (0,1,2,3,4,5)
                combo5.current(0) #set the selected item
                combo5.grid(column=3, row=6,padx=30)

                ll6=Label(Frame2,text="Chicken Junglee Sandwich",fg='red',bg="#aedb9f")
                ll6.grid(row=7,column=1,sticky=W)
                ll66=Label(Frame2,text="₹475",bg="#aedb9f")
                ll66.grid(row=7,column=2)
                bb6=Button(Frame2,text="Choose",command=lambda :click(bb6),bg="#00FFFF")
                bb6.grid(row=7,column=4,padx=30)
                combo6 =ttk.Combobox(Frame2)
                combo6['values']= (0,1,2,3,4,5)
                combo6.current(0) #set the selected item
                combo6.grid(column=3, row=7,padx=30)

                sub=Button(Frame2,text="SUBMIT",command=bill_area,bg="#00FFFF")
                sub.grid(row=8,column=5)

                T = Text(Frame2, height=5, width=45)
                T.grid(row=1,column=5,rowspan=7)
                def click(b):
                    global Total
                    global p1
                    global p2
                    global p3
                    global p4
                    global p5
                    global p6
                    f=open("food.dat","wb")
                    if b==bb1:
                        v1=int(combo.get())
                        p1=str(150*v1)
                        c1=150
                        quote="Choco chip cookie"+" "+'\t'+str(v1)+" "+'\t'+"₹"+p1+"\n"
                        data=["Choco chip cookie",c1,str(v1),p1]
                        record.append(data)
                        T.insert(END, quote)
                    elif b==bb2:
                        v2=int(combo2.get())
                        p2=str(200*v2)
                        c2=200
                        quote="Cashew(salted)"+" "+'\t'+str(v2)+" "+'\t'+"₹"+p2+"\n"
                        data=["Cashew(salted)",c2,str(v2),p2]
                        record.append(data)
                        T.insert(END, quote)
                    elif b==bb3:
                        v3=int(combo3.get())
                        p3=str(350*v3)
                        c3=350
                        quote="Veg Mayo Sandwich"+" "+'\t'+str(v3)+" "+'\t'+"₹"+p3+"\n"
                        data=["Veg Mayo Sandwich",c3,str(v3),p3]
                        record.append(data)
                        T.insert(END, quote)
                    elif b==bb4:
                        v4=int(combo4.get())
                        p4=str(375*v4)
                        c4=375
                        quote="Paneer Tikka Sandwich"+" "+'\t'+str(v4)+" "+'\t'+"₹"+p4+"\n"
                        data=["Paneer Tikka Sandwich",c4,str(v4),p4]
                        record.append(data)
                        T.insert(END, quote)
                    elif b==bb5:
                        v5=int(combo5.get())
                        p5=str(400*v5)
                        c5=400
                        quote="Chicken Tikka Sandwich"+" "+'\t'+str(v5)+" "+'\t'+"₹"+p5+"\n"
                        data=["Chicken Tikka Sandwich",c5,str(v5),p5]
                        record.append(data)
                        T.insert(END, quote)
                    elif b==bb6:
                        v6=int(combo6.get())
                        p6=str(475*v6)
                        c6=475
                        quote='Chicken Junglee Sandwich'+" "+'\t'+str(v6)+" "+'\t'+"₹"+p6+"\n"
                        data=["Chicken Junglee Sandwich",c6,str(v6),p6]
                        record.append(data)
                        T.insert(END, quote)
                        Total=int(int(p1)+int(p2)+int(p3)+int(p4)+int(p5)+int(p6))
                    else:
                        self.root5.mainloop()
                    pickle.dump(record,f)
                    f.close()


            Frame1=Frame(self.root4,bd=20,width=500,height=400,relief=RIDGE,bg="#aedb9f")
            Frame1.grid()
            
            l0=Label(Frame1, text="Do you want food?", font=("Arial bold",16),bg="#aedb9f")
            l0.grid(row=0, column=0)

            b1=Button(Frame1, text="Yes",font=("Helvetica",10),command=Yes,bg="#00FFFF")
            b1.grid(row=1,column=0,padx=0,pady=10)

            b2=Button(Frame1, text="No",font=("Helvetica",10),command=bill_area,bg="#00FFFF")
            b2.grid(row=1,column=1,pady=10)
            self.root4.mainloop()

        def treeview():
            self.root2.withdraw()
            con=mycon.connect(host='localhost',user='root',password='password')
            cur=con.cursor()
            cur.execute("CREATE DATABASE IF NOT EXISTS FLIGHT")
            con.commit()
            cur.execute("USE FLIGHT")
            cur.execute("CREATE TABLE IF NOT EXISTS PASSANGERS(FLIGHT_NO VARCHAR(25),NAME VARCHAR(50),AADHAR_NO VARCHAR(40) PRIMARY KEY,AGE INT, GENDER VARCHAR(20),FOREIGN KEY(FLIGHT_NO) REFERENCES FLIGHTS(FLIGHT_NO))")
            con.commit()
            self.root3=Tk()
            self.root3.title("EMERALD AIRLINES")
            self.root3.grid_rowconfigure(0, weight=1)
            self.root3.grid_columnconfigure(0, weight=1)
            Rightframe=Frame(self.root3,bd=20,width=700,height=700,relief=RIDGE,bg="#aedb9f")
            Rightframe.grid()
            self.name_label = Label(Rightframe, text="NAME :",font=('Helvetica',12),bg="#aedb9f")
            self.name_entry = Entry(Rightframe)
            self.name_entry.insert(END,'FULL NAME')
            self.name_label.grid(row=0, column=0, sticky=W)
            self.name_entry.grid(row=0, column=1)

            self.adnumber_label = Label(Rightframe, text="AADHAR NO :",font=('Helvetica',12),bg="#aedb9f")
            self.adnumber_entry = Entry(Rightframe)
            self.adnumber_label.grid(row=1, column=0, sticky=W)
            self.adnumber_entry.grid(row=1, column=1)

            self.age_label = Label(Rightframe, text="AGE :",font=('Helvetica',12),bg="#aedb9f")
            self.age_entry = Entry(Rightframe)
            self.age_label.grid(row=2, column=0, sticky=W)
            self.age_entry.grid(row=2, column=1)

            self.gender_label = Label(Rightframe, text="GENDER :",font=('Helvetica',12),bg="#aedb9f")
            self.gender_entry = Entry(Rightframe)
            self.gender_label.grid(row=3, column=0, sticky=W)
            self.gender_entry.grid(row=3, column=1)
            
            self.insert_button = Button(Rightframe, text="INSERT",font=('Helvetica',10), command=lambda :insert_data(self),bg="#00FFFF")
            self.insert_button.grid(row=4, column=1)

            self.tree = ttk.Treeview(Rightframe,columns=('NAME', 'AADHAR NO.','AGE','GENDER'))

            self.tree.heading('#0', text='S.NO')
            self.tree.heading('#1', text='NAME')
            self.tree.heading('#2', text='AADHAR NO.')
            self.tree.heading('#3', text='AGE')
            self.tree.heading('#4', text='GENDER')

            self.tree.column('#0', stretch=YES)
            self.tree.column('#1', stretch=YES)
            self.tree.column('#2', stretch=YES)
            self.tree.column('#3', stretch=YES)
            self.tree.column('#4', stretch=YES)

            self.tree.grid(row=5, columnspan=4, sticky='nsew')
            self.treeview = self.tree

            self.id = 1
            self.iid = 0
            
            self.submit_details=Button(Rightframe,text='SUBMIT',font=('Helvetica',10),command=submit_d,bg="#00FFFF")
            self.submit_details.grid(row=7,column=1)
            

        def insert_data(self):
            if self.iid==seats:
                self.insert_button.config(state='disabled')
                messagebox.showwarning("Warning", "You have already entered the details of all the passangers")
            else:
                query="INSERT INTO PASSANGERS (FLIGHT_NO,NAME,AADHAR_NO,AGE,GENDER) VALUES (%s,%s,%s,%s,%s)"
                values=(fnum,self.name_entry.get(),
                                     self.adnumber_entry.get(),self.age_entry.get(),self.gender_entry.get())
                cur.execute(query,values)
                con.commit()
                self.treeview.insert('', 'end', iid=self.iid,text =str(self.id),
                             values=(self.name_entry.get(),
                                     self.adnumber_entry.get(),self.age_entry.get(),self.gender_entry.get()))
                self.iid = self.iid + 1
                self.id = self.id + 1
                self.name_entry.delete(0,END)
                self.adnumber_entry.delete(0,END)
                self.age_entry.delete(0,END)
                self.gender_entry.delete(0,END)
        def seat():
            con=mycon.connect(host='localhost',user='root',password='password')
            cur=con.cursor()
            cur.execute("CREATE DATABASE IF NOT EXISTS FLIGHT")
            con.commit()
            cur.execute("USE FLIGHT")
            cur.execute("CREATE TABLE IF NOT EXISTS SEAT(BUTTON VARCHAR(50),VALUE INT DEFAULT 0)")
            con.commit()
            global c
            c=[]
            def changeColor(btn):
                query="SELECT * FROM SEAT WHERE BUTTON='{}'".format(btn)
                cur.execute(query)
                result=cur.fetchall()
                if cur.rowcount==0:
                    # Use your bg argument instead of highlight background
                    btn.configure(bg='#ff0800')
                    query="INSERT INTO SEAT VALUES ('{}',1)".format(btn)
                    cur.execute(query)
                    con.commit()
                    if btn==button1:
                        c.append("A1")
                    if btn==button2:
                        c.append("A2")
                    if btn==button21:
                        c.append("A3")
                    if btn==button22:
                        c.append("A4")
                    if btn==button3:
                        c.append("B1")
                    if btn==button4:
                        c.append("B2")
                    if btn==button23:
                        c.append("B3")
                    if btn==button24:
                        c.append("B4")
                    if btn==button5:
                        c.append("C1")
                    if btn==button6:
                        c.append("C2")
                    if btn==button25:
                        c.append("C3")
                    if btn==button26:
                        c.append("C4")
                    if btn==button7:
                        c.append("D1")
                    if btn==button8:
                        c.append("D2")
                    if btn==button27:
                        c.append("D3")
                    if btn==button28:
                        c.append("D4")
                    if btn==button9:
                        c.append("E1")
                    if btn==button10:
                        c.append("E2")
                    if btn==button29:
                        c.append("E3")
                    if btn==button30:
                        c.append("E4")
                    if btn==button11:
                        c.append("F1")
                    if btn==button12:
                        c.append("F2")
                    if btn==button31:
                        c.append("F3")
                    if btn==button32:
                        c.append("F4")
                    if btn==button13:
                        c.append("G1")
                    if btn==button33:
                        c.append("G2")
                    if btn==button14:
                        c.append("G3")
                    if btn==button34:
                        c.append("G4")
                    if btn==button15:
                        c.append("H1")
                    if btn==button16:
                        c.append("H2")
                    if btn==button35:
                        c.append("H3")
                    if btn==button36:
                        c.append("H4")
                    if btn==button17:
                        c.append("I1")
                    if btn==button18:
                        c.append("I2")
                    if btn==button37:
                        c.append("I3")
                    if btn==button38:
                        c.append("I4")
                    if btn==button19:
                        c.append("J1")
                    if btn==button20:
                        c.append("J2")
                    if btn==button39:
                        c.append("J3")
                    if btn==button40:
                        c.append("J4")
                    if btn==button41:
                        c.append('K1')
                    if btn==button42:
                        c.append("K2")
                    if btn==button43:
                        c.append("K3")
                    if btn==button44:
                        c.append("K4")
                    if btn==button45:
                        c.append("L1")
                    if btn==button46:
                        c.append("L2")
                    if btn==button47:
                        c.append("L3")
                    if btn==button48:
                        c.append("L4")
                    if btn==button49:
                        c.append("M1")
                    if btn==button50:
                        c.append("M2")
                    if btn==button51:
                        c.append("M3")
                    if btn==button52:
                        c.append("M4")
                    if btn==button53:
                        c.append("N1")
                    if btn==button54:
                        c.append("N2")
                    if btn==button55:
                        c.append("N3")
                    if btn==button56:
                        c.append("N4")
                    if btn==button57:
                        c.append("O1")
                    if btn==button58:
                        c.append("O2")
                    if btn==button59:
                        c.append("O3")
                    if btn==button60:
                        c.append("O4")
                else:
                    messagebox.showwarning("Warning", "Sorry , this seat has already been booked .\n Please book a different seat .")
                    btn.configure(highlightbackground='#A9A9A9')

            self.root2=Tk()
            self.root2.title("SEATING ARRANGEMENT")
            frame=Frame(self.root2,bd=20,width=1200,height=1200,relief=RIDGE,bg="#aedb9f")
            frame.grid()
            button1=Button(frame,text="A1",width=8,command=lambda: changeColor(button1))
            button1.grid(row=0,column=0)
            button2=Button(frame,text="A2",width=8,command=lambda: changeColor(button2))
            button2.grid(row=0,column=1)
            button3=Button(frame,text="B1",width=8,command=lambda: changeColor(button3))
            button3.grid(row=1,column=0)
            button4=Button(frame,text="B2",width=8,command=lambda: changeColor(button4))
            button4.grid(row=1,column=1)
            button5=Button(frame,text="C1",width=8,command=lambda: changeColor(button5))
            button5.grid(row=2,column=0)
            button6=Button(frame,text="C2",width=8,command=lambda: changeColor(button6))
            button6.grid(row=2,column=1)
            button7=Button(frame,text="D1",width=8,command=lambda: changeColor(button7))
            button7.grid(row=3,column=0)
            button8=Button(frame,text="D2",width=8,command=lambda: changeColor(button8))
            button8.grid(row=3,column=1)
            button9=Button(frame,text="E1",width=8,command=lambda: changeColor(button9))
            button9.grid(row=4,column=0)
            button10=Button(frame,text="E2",width=8,command=lambda: changeColor(button10))
            button10.grid(row=4,column=1)
            button11=Button(frame,text="F1",width=8,command=lambda: changeColor(button11))
            button11.grid(row=5,column=0)
            button12=Button(frame,text="F2",width=8,command=lambda: changeColor(button12))
            button12.grid(row=5,column=1)
            button13=Button(frame,text="G1",width=8,command=lambda: changeColor(button13))
            button13.grid(row=6,column=0)
            button14=Button(frame,text="G2",width=8,command=lambda: changeColor(button14))
            button14.grid(row=6,column=1)
            button15=Button(frame,text="H1",width=8,command=lambda: changeColor(button15))
            button15.grid(row=7,column=0)
            button16=Button(frame,text="H2",width=8,command=lambda: changeColor(button16))
            button16.grid(row=7,column=1)
            button17=Button(frame,text="I1",width=8,command=lambda: changeColor(button17))
            button17.grid(row=8,column=0)
            button18=Button(frame,text="I2",width=8,command=lambda: changeColor(button18))
            button18.grid(row=8,column=1)
            button19=Button(frame,text="J1",width=8,command=lambda: changeColor(button19))
            button19.grid(row=9,column=0)
            button20=Button(frame,text="J2",width=8,command=lambda: changeColor(button20))
            button20.grid(row=9,column=1)

            label1=Label(frame,text="       ",padx=20,bg="#aedb9f").grid(row=0,column=2)

            button21=Button(frame,text="A3",width=8,command=lambda: changeColor(button21))
            button21.grid(row=0,column=3,sticky='E')
            button22=Button(frame,text="A4",width=8,command=lambda: changeColor(button22))
            button22.grid(row=0,column=4,sticky='E')
            button23=Button(frame,text="B3",width=8,command=lambda: changeColor(button23))
            button23.grid(row=1,column=3,sticky='E')
            button24=Button(frame,text="B4",width=8,command=lambda: changeColor(button24))
            button24.grid(row=1,column=4,sticky='E')
            button25=Button(frame,text="C3",width=8,command=lambda: changeColor(button25))
            button25.grid(row=2,column=3,sticky='E')
            button26=Button(frame,text="C4",width=8,command=lambda: changeColor(button26))
            button26.grid(row=2,column=4,sticky='E')
            button27=Button(frame,text="D3",width=8,command=lambda: changeColor(button27))
            button27.grid(row=3,column=3,sticky='E')
            button28=Button(frame,text="D4",width=8,command=lambda: changeColor(button28))
            button28.grid(row=3,column=4,sticky='E')
            button29=Button(frame,text="E3",width=8,command=lambda: changeColor(button29))
            button29.grid(row=4,column=3,sticky='E')
            button30=Button(frame,text="E4",width=8,command=lambda: changeColor(button30))
            button30.grid(row=4,column=4,sticky='E')
            button31=Button(frame,text="F3",width=8,command=lambda: changeColor(button31))
            button31.grid(row=5,column=3,sticky='E')
            button32=Button(frame,text="F4",width=8,command=lambda: changeColor(button32))
            button32.grid(row=5,column=4,sticky='E')
            button33=Button(frame,text="G3",width=8,command=lambda: changeColor(button33))
            button33.grid(row=6,column=3,sticky='E')
            button34=Button(frame,text="G4",width=8,command=lambda: changeColor(button34))
            button34.grid(row=6,column=4,sticky='E')
            button35=Button(frame,text="H3",width=8,command=lambda: changeColor(button35))
            button35.grid(row=7,column=3,sticky='E')
            button36=Button(frame,text="H4",width=8,command=lambda: changeColor(button36))
            button36.grid(row=7,column=4,sticky='E')
            button37=Button(frame,text="I3",width=8,command=lambda: changeColor(button37))
            button37.grid(row=8,column=3,sticky='E')
            button38=Button(frame,text="I4",width=8,command=lambda: changeColor(button38))
            button38.grid(row=8,column=4,sticky='E')
            button39=Button(frame,text="J3",width=8,command=lambda: changeColor(button39))
            button39.grid(row=9,column=3,sticky='E')
            button40=Button(frame,text="J4",width=8,command=lambda: changeColor(button40))
            button40.grid(row=9,column=4,sticky='E')

            label1=Label(frame,text="       ",padx=20,bg="#aedb9f").grid(row=10,column=2)

            button41=Button(frame,text="K1",width=8,command=lambda: changeColor(button41))
            button41.grid(row=10,column=0,sticky='E')
            button42=Button(frame,text="K2",width=8,command=lambda: changeColor(button42))
            button42.grid(row=10,column=1,sticky='E')
            button43=Button(frame,text="K3",width=8,command=lambda: changeColor(button43))
            button43.grid(row=10,column=3,sticky='E')
            button44=Button(frame,text="K4",width=8,command=lambda: changeColor(button44))
            button44.grid(row=10,column=4,sticky='E')
            button45=Button(frame,text="L1",width=8,command=lambda: changeColor(button45))
            button45.grid(row=11,column=0,sticky='E')
            button46=Button(frame,text="L2",width=8,command=lambda: changeColor(button46))
            button46.grid(row=11,column=1,sticky='E')
            button47=Button(frame,text="L3",width=8,command=lambda: changeColor(button47))
            button47.grid(row=11,column=3,sticky='E')
            button48=Button(frame,text="L4",width=8,command=lambda: changeColor(button48))
            button48.grid(row=11,column=4,sticky='E')
            button49=Button(frame,text="M1",width=8,command=lambda: changeColor(button49))
            button49.grid(row=12,column=0,sticky='E')
            button50=Button(frame,text="M2",width=8,command=lambda: changeColor(button50))
            button50.grid(row=12,column=1,sticky='E')
            button51=Button(frame,text="M3",width=8,command=lambda: changeColor(button51))
            button51.grid(row=12,column=3,sticky='E')
            button52=Button(frame,text="M4",width=8,command=lambda: changeColor(button52))
            button52.grid(row=12,column=4,sticky='E')
            button53=Button(frame,text="N1",width=8,command=lambda: changeColor(button53))
            button53.grid(row=13,column=0,sticky='E')
            button54=Button(frame,text="N2",width=8,command=lambda: changeColor(button54))
            button54.grid(row=13,column=1,sticky='E')
            button55=Button(frame,text="N3",width=8,command=lambda: changeColor(button55))
            button55.grid(row=13,column=3,sticky='E')
            button56=Button(frame,text="N4",width=8,command=lambda: changeColor(button56))
            button56.grid(row=13,column=4,sticky='E')
            button57=Button(frame,text="O1",width=8,command=lambda: changeColor(button57))
            button57.grid(row=14,column=0,sticky='E')
            button58=Button(frame,text="O2",width=8,command=lambda: changeColor(button58))
            button58.grid(row=14,column=1,sticky='E')
            button59=Button(frame,text="O3",width=8,command=lambda: changeColor(button59))
            button59.grid(row=14,column=3,sticky='E')
            button60=Button(frame,text="O4",width=8,command=lambda: changeColor(button60))
            button60.grid(row=14,column=4,sticky='E')

            
            button=Button(frame,text="DONE",command=treeview)
            button.grid(row=16,column=2)


            self.root2.mainloop()

        def hello(b):
            if isclicked==False:
                if b=='ECONOMY':
                    self.p1.delete(0,END)
                    self.p1.insert(END,'9000')
                    self.p2.delete(0,END)
                    self.p2.insert(END,'10800')
                    self.p3.delete(0,END)
                    self.p3.insert(END,'7280')
                    self.p4.delete(0,END)
                    self.p4.insert(END,'12000')
                    self.p5.delete(0,END)
                    self.p5.insert(END,'11200')
                elif b=='PREMIUM ECONOMY':
                    self.p1.delete(0,END)
                    self.p1.insert(END,'12800')
                    self.p2.delete(0,END)
                    self.p2.insert(END,'17800')
                    self.p3.delete(0,END)
                    self.p3.insert(END,'15800')
                    self.p4.delete(0,END)
                    self.p4.insert(END,'16200')
                    self.p5.delete(0,END)
                    self.p5.insert(END,'11900')
                elif b=='BUISNESS':
                    self.p1.delete(0,END)
                    self.p1.insert(END,'19900')
                    self.p2.delete(0,END)
                    self.p2.insert(END,'17900')
                    self.p3.delete(0,END)
                    self.p3.insert(END,'19900')
                    self.p4.delete(0,END)
                    self.p4.insert(END,'19600')
                    self.p5.delete(0,END)
                    self.p5.insert(END,'20900')
                else:
                    messagebox.showwarning("Warning", "Sorry , you have not selected a category")
            else:
                if b=='ECONOMY':
                    pass
                elif b=='PREMIUM ECONOMY':
                    self.p1.delete(0,END)
                    self.p1.insert(END,'8900')
                    self.p2.delete(0,END)
                    self.p2.insert(END,'8400')
                    self.p3.delete(0,END)
                    self.p3.insert(END,'10900')
                    self.p4.delete(0,END)
                    self.p4.insert(END,'10600')
                    self.p5.delete(0,END)
                    self.p5.insert(END,'9900')
                elif b=='BUISNESS':
                    self.p1.delete(0,END)
                    self.p1.insert(END,'10900')
                    self.p2.delete(0,END)
                    self.p2.insert(END,'11400')
                    self.p3.delete(0,END)
                    self.p3.insert(END,'13900')
                    self.p4.delete(0,END)
                    self.p4.insert(END,'15600')
                    self.p5.delete(0,END)
                    self.p5.insert(END,'18900')
                else:
                    messagebox.showwarning("Warning", "Sorry , you have not selected a category")
        def clickedme(btn):
            global total
            global Total
            if btn==self.b1:
                total+=int(self.p1.get())
            elif btn==self.b2:
                total+=int(self.p2.get())
            elif btn==self.b3:
                total+=int(self.p3.get())
            elif btn==self.b4:
                total+=int(self.p4.get())
            elif btn==self.b5:
                total+=int(self.p5.get())
            else:
                total=0
        def subm():
            self.root1.withdraw()
            seat()
        def search():
            self.root.withdraw()
            self.root1=Tk()
            self.root1.title("EMERALD AIRLINES")
            Leftframe=Frame(self.root1,bd=20,width=1200,height=1200,relief=RIDGE,bg="#aedb9f")
            Leftframe.grid()
            self.l0=Label(Leftframe, text="Choose your flight",font=("Arial bold",22),bg="#aedb9f")
            self.l0.grid(row=0, column=0,padx=10)
            
            self.l00=Label(Leftframe,text="Flight Timings",font=("Arial bold",18),bg="#aedb9f")
            self.l00.grid(row=1,column=0, padx=10, pady=20)
            self.l01=Label(Leftframe,text="Price(In ₹)",font=("Arial bold",18),bg="#aedb9f")
            self.l01.grid(row=1,column=1,padx=20,pady=20)
            
            self.l1=Label(Leftframe,text="07:00 → 09:00",font=("Helventica",12),bg="#aedb9f")
            self.l1.grid(row=2,column=0, padx=10, pady=20)
            self.p1=Entry(Leftframe,font=("Helventica",12))
            self.p1.insert(END,'5000')
            self.p1.grid(row=2,column=1)
            self.b1=Button(Leftframe,text='✓',command=lambda: clickedme(self.b1),bg="#00FFFF")
            self.b1.grid(row=2,column=2)
            
            self.l2=Label(Leftframe,text="08:30 → 10:30",font=("Helventica",12),bg="#aedb9f")
            self.l2.grid(row=3,column=0, padx=10, pady=20)
            self.p2=Entry(Leftframe,font=("Helventica",12))
            self.p2.insert(END,"5900")
            self.p2.grid(row=3,column=1)
            self.b2=Button(Leftframe,text='✓',command=lambda: clickedme(self.b2),bg="#00FFFF")
            self.b2.grid(row=3,column=2)
            
            self.l3=Label(Leftframe,text="11:00 → 13:00",font=("Helventica",12),bg="#aedb9f")
            self.l3.grid(row=4,column=0, padx=10, pady=20)
            self.p3=Entry(Leftframe,font=("Helventica",12))
            self.p3.insert(END,"7640")
            self.p3.grid(row=4,column=1)
            self.b3=Button(Leftframe,text='✓',command=lambda: clickedme(self.b3),bg="#00FFFF")
            self.b3.grid(row=4,column=2)
            
            self.l4=Label(Leftframe,text="13:40 → 15:45",font=("Helventica",12),bg="#aedb9f")
            self.l4.grid(row=5,column=0, padx=10, pady=20)
            self.p4=Entry(Leftframe,font=("Helventica",12))
            self.p4.insert(END,"8500")
            self.p4.grid(row=5,column=1)
            self.b4=Button(Leftframe,text='✓',command=lambda: clickedme(self.b4),bg="#00FFFF")
            self.b4.grid(row=5,column=2)
            
            self.l5=Label(Leftframe,text="18:40 → 20:40",font=("Helventica",12),bg="#aedb9f")
            self.l5.grid(row=6,column=0, padx=10, pady=20)
            self.p5=Entry(Leftframe,font=("Helventica",12))
            self.p5.insert(END,"9600")
            self.p5.grid(row=6,column=1)
            self.b5=Button(Leftframe,text='✓',command=lambda: clickedme(self.b5),bg="#00FFFF")
            self.b5.grid(row=6,column=2)

            self.l6=Label(Leftframe,text=" ",font=('Calibri',17),bg="#aedb9f")
            self.l6.grid(row=7,column=0)
            hello(self.class_combo1.get())

            self.submit=Button(Leftframe,text='SUBMIT',font=('Helvetica',12),width=13,command=subm,bg="#00FFFF").place(x=190,y=425)
            #self.submit.grid(row=7,column=0)
            self.root1.mainloop()

        def submit():
            con=mycon.connect(host='localhost',user='root',password='password')
            cur=con.cursor()

            cur.execute("CREATE DATABASE IF NOT EXISTS FLIGHT")
            con.commit()
            cur.execute("USE FLIGHT")
            cur.execute("CREATE TABLE IF NOT EXISTS FLIGHTS(FLIGHT_NO VARCHAR(25) PRIMARY KEY,ORIGIN VARCHAR(50),DESTINATION VARCHAR(50),DEPART DATE,RETURN_D DATE,ADULT INT,CHILD INT,CLASS VARCHAR(75))")
            con.commit()
            global seats
            if isclicked==True:
                query="SELECT * FROM DETAILS WHERE ORIGIN ='{}' AND DESTINATION ='{}'".format(self.origin_entry.get(),self.destination_entry.get())
                cur.execute(query)
                result=cur.fetchall()
                if cur.rowcount==0:
                    messagebox.showwarning("Warning", "Sorry , for the inconvenience")
                else:
                    query="INSERT INTO FLIGHTS (FLIGHT_NO,ORIGIN,DESTINATION,DEPART,ADULT,CHILD,CLASS) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                    values=(fnum,self.origin_entry.get(),self.destination_entry.get(),self.depart_entry.get(),self.adult_entry.get(),self.child_entry.get(),self.class_combo1.get())
                    cur.execute(query,values)
                    con.commit()
                    seats=int(int(self.child_entry.get())+int(self.adult_entry.get()))
                    search()
            else:
                query="SELECT * FROM DETAILS WHERE ORIGIN ='{}' AND DESTINATION ='{}'".format(self.origin_entry.get(),self.destination_entry.get())
                cur.execute(query)
                result=cur.fetchall()
                if cur.rowcount==0: 
                    messagebox.showwarning("Warning", "Sorry , for the inconvenience")
                else:
                    query="INSERT INTO FLIGHTS (FLIGHT_NO,ORIGIN,DESTINATION,DEPART,RETURN_D,ADULT,CHILD,CLASS) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                    values=(fnum,self.origin_entry.get(),self.destination_entry.get(),self.depart_entry.get(),self.return_entry.get(),self.adult_entry.get(),self.child_entry.get(),self.class_combo1.get())
                    cur.execute(query,values)
                    con.commit()
                    seats=int(int(self.child_entry.get())+int(self.adult_entry.get()))
                    search()

        self.submit=Button(Mainframe,text="SUBMIT",font=('Helvetica',16),width=13,bg="#00FFFF",command=submit).place(x=190,y=400)

root=Tk()
application=FLIGHT(root)
root.mainloop()

