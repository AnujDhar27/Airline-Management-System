from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import mysql.connector as mycon
from tkinter import messagebox 
from tkinter import filedialog

isclicked=False
total=0
seats=0
p1=0
p2=0
p3=0
p4=0
p5=0
p6=0
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
		values=[('KOLKATA','MUMBAI'),('KOLKATA','DELHI'),('MUMBAI','DELHI'),("K","M")]
		for i in range(0,len(values)):
			query="INSERT INTO DETAILS (ORIGIN,DESTINATION) VALUES (%s,%s)"
			cur.execute(query,values[i])
			con.commit()

		self.class_combo1=StringVar()

		Mainframe=Frame(self.root,bd=20,width=700,height=700,relief=RIDGE,bg="#aedb9f")
		Mainframe.grid()

		def clickme(btn):
			btn.configure(highlightbackground='#008000')
			global isclicked
			if btn==self.button2:
				self.return_label.config(state='disabled')
				self.return_entry.config(state='disabled')
				self.return_button.config(state='disabled')
				isclicked=True

		self.label=Label(Mainframe,text="EMERALD AIRLINES",font=("Arial bold",22),bg="#aedb9f")
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

		self.class_label=Label(Mainframe,text=' ',font=("Helvetica",22),bg="#aedb9f")
		self.class_label.grid(row=9,column=0,padx=5,pady=5,sticky=W)

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
			self.root4=Tk()
			self.root3.title("AIRLINE MANAGEMENT SYSTEM")
			Billframe=Frame(self.root4,bd=20,width=700,height=700,relief=RIDGE)
			Billframe.grid()
			T1 = Text(Billframe, height=200, width=100,font=("Arial bold",18))
			T1.grid(row=0,column=0,rowspan=7)
			T1.insert(END,"====================================================================================================")
			T1.insert(END, "                                         EMERALD AIRLINES \n")
			T1.insert(END,"                                       CONTACT NO :033-9787899  \n          "                                   )
			T1.insert(END,"\n")
			T1.insert(END,"\n")
			T1.insert(END,"\n")
			T1.insert(END,"====================================================================================================\n")
			T1.insert(END,"LOGIN ID :")
			T1.insert(END,"\n")
			T1.insert(END,"FLIGHT NO :")
			T1.insert(END,"\n")
			T1.insert(END,f"ORIGIN :                           {self.origin_entry.get()}\n")
			T1.insert(END,f"DESTINATION :                      {self.destination_entry.get()}\n")
			T1.insert(END,f"DEPARTURE :                        {self.depart_entry.get()}\n")
			T1.insert(END,f"PASSANGERS :            ADULT  :   {self.adult_entry.get()}\n")
			T1.insert(END,f"                        CHILD  :   {self.child_entry.get()}\n")
			T1.insert(END,"\n")
			self.root4.mainloop()
		def submit_d():
			self.root3=Tk()
			self.root3.title("EMERALD AIRLINES")
			def Yes():
				self.mast=Tk()
				self.mast.title("EMERALD AIRLINES")
				self.mast.geometry("1200x200")
				ll0=Label(self.mast,text="EMERALD AIRLINES MENU",font=("Arial bold",16))
				ll0.grid(row=0,column=0)
				ll00=Label(self.mast,text="YOUR ORDER",font=("Arial bold",10))
				ll00.grid(row=2,column=5,padx=50)
				ll1=Label(self.mast,text="Choco Chip Cookie",fg='green')
				ll1.grid(row=2,column=1,sticky=W)
				ll11=Label(self.mast,text="₹150")
				ll11.grid(row=2,column=2)
				bb1=Button(self.mast,text="Choose",command=lambda :click(bb1))
				bb1.grid(row=2,column=4,padx=30)
				combo =ttk.Combobox(self.mast)
				combo['values']= (0,1,2,3,4,5)
				combo.current(0) #set the selected item
				combo.grid(column=3, row=2,padx=30)

				ll2=Label(self.mast,text="Cashew(salted)",fg='green')
				ll2.grid(row=3,column=1,sticky=W)
				ll22=Label(self.mast,text="₹200")
				ll22.grid(row=3,column=2)
				bb2=Button(self.mast,text="Choose",command=lambda :click(bb2))
				bb2.grid(row=3,column=4,padx=30)
				combo2 =ttk.Combobox(self.mast)
				combo2['values']= (0,1,2,3,4,5)
				combo2.current(0) #set the selected item
				combo2.grid(column=3, row=3,padx=30)

				ll3=Label(self.mast,text="Veg Mayo Sandwich",fg='green')
				ll3.grid(row=4,column=1,sticky=W)
				ll33=Label(self.mast,text="₹350")
				ll33.grid(row=4,column=2)
				bb3=Button(self.mast,text="Choose",command=lambda :click(bb3))
				bb3.grid(row=4,column=4,padx=30)
				combo3 =ttk.Combobox(self.mast)
				combo3['values']= (0,1,2,3,4,5)
				combo3.current(0) #set the selected item
				combo3.grid(column=3, row=4,padx=30)

				ll4=Label(self.mast,text="Paneer Tikka Sandwich",fg='green')
				ll4.grid(row=5,column=1,sticky=W)
				ll44=Label(self.mast,text="₹350")
				ll44.grid(row=5,column=2)
				bb4=Button(self.mast,text="Choose",command=lambda :click(bb4))
				bb4.grid(row=5,column=4,padx=30)
				combo4 =ttk.Combobox(self.mast)
				combo4['values']= (0,1,2,3,4,5)
				combo4.current(0) #set the selected item
				combo4.grid(column=3, row=5,padx=30)

				ll5=Label(self.mast,text="Chicken Tikka Sandwich",fg='red')
				ll5.grid(row=6,column=1,sticky=W)
				ll55=Label(self.mast,text="₹375")
				ll55.grid(row=6,column=2)
				bb5=Button(self.mast,text="Choose",command=lambda :click(bb5))
				bb5.grid(row=6,column=4,padx=30)
				combo5 =ttk.Combobox(self.mast)
				combo5['values']= (0,1,2,3,4,5)
				combo5.current(0) #set the selected item
				combo5.grid(column=3, row=6,padx=30)

				ll6=Label(self.mast,text="Chicken Junglee Sandwich",fg='red')
				ll6.grid(row=7,column=1,sticky=W)
				ll33=Label(self.mast,text="₹375")
				ll33.grid(row=7,column=2)
				bb6=Button(self.mast,text="Choose",command=lambda :click(bb6))
				bb6.grid(row=7,column=4,padx=30)
				combo6 =ttk.Combobox(self.mast)
				combo6['values']= (0,1,2,3,4,5)
				combo6.current(0) #set the selected item
				combo6.grid(column=3, row=7,padx=30)

				sub=Button(self.mast,text="SUBMIT",command=bill_area)
				sub.grid(row=8,column=1)

				T = Text(self.mast, height=5, width=50)
				T.grid(row=1,column=5,rowspan=7)
				def click(b):
					global p1
					global p2
					global p3
					global p4
					global p5
					global p6
					if b==bb1:
						v1=int(combo.get())
						p1=str(150*v1)
						quote="Choco chip cookie"+" "+'\t'+str(v1)+" "+'\t'+"₹"+p1+"\n"
						T.insert(END, quote)
					elif b==bb2:
						v2=int(combo2.get())
						p2=str(200*v2)
						quote="Cashew(salted)"+" "+'\t'+str(v2)+" "+'\t'+"₹"+p2+"\n"
						T.insert(END, quote)
					elif b==bb3:
						v3=int(combo3.get())
						p3=str(350*v3)
						quote="Veg Mayo Sandwich"+" "+'\t'+str(v3)+" "+'\t'+"₹"+p3+"\n"
						T.insert(END, quote)
					elif b==bb4:
						v4=int(combo4.get())
						p4=str(350*v4)
						quote="Paneer Tikka Sandwich"+" "+'\t'+str(v4)+" "+'\t'+"₹"+p4+"\n"
						T.insert(END, quote)
					elif b==bb5:
						v5=int(combo5.get())
						p5=str(375*v5)
						quote="Chicken Tikka Sandwich"+" "+'\t'+str(v5)+" "+'\t'+"₹"+p5+"\n"
						T.insert(END, quote)
					elif b==bb6:
						v6=int(combo6.get())
						p6=str(375*v6)
						quote='Chicken Junglee Sandwich'+" "+'\t'+str(v6)+" "+'\t'+"₹"+p6+"\n"
						T.insert(END, quote)
					else:
						self.mast.mainloop()   
			l0=Label(self.root3, text="Do you want food?", font=("Arial bold",16))
			l0.grid(row=0, column=0)

			b1=Button(self.root3, text="Yes",command=Yes)
			b1.grid(row=5,column=0,pady=10)

			b2=Button(self.root3, text="No",command=self.root.quit)
			b2.grid(row=5,column=1,pady=10)
			self.root3.mainloop()

		def treeview():
			self.root2=Tk()
			self.root2.title("EMERALD AIRLINES")
			self.root2.grid_rowconfigure(0, weight=1)
			self.root2.grid_columnconfigure(0, weight=1)
			Rightframe=Frame(self.root2,bd=20,width=700,height=700,relief=RIDGE,bg="#aedb9f")
			Rightframe.grid()
			self.name_label = Label(Rightframe, text="NAME :",bg="#aedb9f")
			self.name_entry = Entry(Rightframe)
			self.name_entry.insert(END,'FULL NAME')
			self.name_label.grid(row=0, column=0, sticky=W)
			self.name_entry.grid(row=0, column=1)

			self.adnumber_label = Label(Rightframe, text="AADHAR NO :",bg="#aedb9f")
			self.adnumber_entry = Entry(Rightframe)
			self.adnumber_label.grid(row=1, column=0, sticky=W)
			self.adnumber_entry.grid(row=1, column=1)

			self.age_label = Label(Rightframe, text="AGE :",bg="#aedb9f")
			self.age_entry = Entry(Rightframe)
			self.age_label.grid(row=2, column=0, sticky=W)
			self.age_entry.grid(row=2, column=1)

			self.gender_label = Label(Rightframe, text="GENDER :",bg="#aedb9f")
			self.gender_entry = Entry(Rightframe)
			self.gender_label.grid(row=3, column=0, sticky=W)
			self.gender_entry.grid(row=3, column=1)

			self.notice_label = Label(Rightframe, text="Please enter the passenger details",font=("Arial Bold",12),bg="#aedb9f").place(x=650,y=30)
			#self.notice_label.grid(row=0,column=3)

			self.submit_button = Button(Rightframe, text="Insert", command=lambda :insert_data(self),bg="#00FFFF")
			self.submit_button.grid(row=4, column=1, sticky=W)

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

			self.submit_details=Button(Rightframe,text='SUBMIT',command=submit_d,bg="#00FFFF")
			self.submit_details.grid(row=6,column=0)

		def insert_data(self):
			self.treeview.insert('', 'end', iid=self.iid,text =str(self.id),
                             values=(self.name_entry.get(),
                                     self.adnumber_entry.get(),self.age_entry.get(),self.gender_entry.get()))
			self.iid = self.iid + 1
			self.id = self.id + 1
			self.name_entry.delete(0,END)
			self.adnumber_entry.delete(0,END)
			self.age_entry.delete(0,END)
			self.gender_entry.delete(0,END)

		def hello(b):
			if b=='ECONOMY':
				pass
			elif b=='PREMIUM ECONOMY':
				self.p1.delete(0,END)
				self.p1.insert(END,'6900')
				self.p2.delete(0,END)
				self.p2.insert(END,'7400')
				self.p3.delete(0,END)
				self.p3.insert(END,'8900')
				self.p4.delete(0,END)
				self.p4.insert(END,'9600')
				self.p5.delete(0,END)
				self.p5.insert(END,'10900')
			elif b=='BUISNESS':
				self.p1.delete(0,END)
				self.p1.insert(END,'10900')
				self.p2.delete(0,END)
				self.p2.insert(END,'11400')
				self.p3.delete(0,END)
				self.p3.insert(END,'12900')
				self.p4.delete(0,END)
				self.p4.insert(END,'14600')
				self.p5.delete(0,END)
				self.p5.insert(END,'16900')
			else:
				messagebox.showwarning("Warning", "Sorry , you have not selected a category")
		def clickedme(btn):
			global total
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
			if total==0:
				messagebox.showwarning("Warning", "Sorry , you have not selected a category")
			else:
				treeview()
		def search():
			self.root1=Tk()
			self.root1.title("EMERALD AIRLINES")
			Leftframe=Frame(self.root1,bd=20,width=1200,height=1200,relief=RIDGE,bg="#aedb9f")
			Leftframe.grid()
			self.l0=Label(Leftframe, text="Choose your flight",font=("Arial bold",22),b g="#aedb9f")
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

			self.l6=Label(Leftframe,text=" ",bg="#aedb9f")
			self.l6.grid(row=7,column=0, padx=10, pady=10)
			
			hello(self.class_combo1.get())

			self.submit=Button(Leftframe,text='SUBMIT',command=subm,bg="#00FFFF").place(x=200,y=430)

			self.root1.mainloop()

		def submit():
			con=mycon.connect(host='localhost',user='root',password='password')
			cur=con.cursor()

			cur.execute("CREATE DATABASE IF NOT EXISTS FLIGHT")
			con.commit()
			cur.execute("USE FLIGHT")
			cur.execute("CREATE TABLE IF NOT EXISTS FLIGHTS(ORIGIN VARCHAR(50),DESTINATION VARCHAR(50),DEPART DATE,RETURN_D DATE,ADULT INT,CHILD INT,CLASS VARCHAR(75))")
			con.commit()
			if isclicked==True:
				query="SELECT * FROM DETAILS WHERE ORIGIN ='{}' AND DESTINATION ='{}'".format(self.origin_entry.get(),self.destination_entry.get())
				cur.execute(query)
				result=cur.fetchall()
				if cur.rowcount==0:
					messagebox.showwarning("Warning", "Sorry , for the inconvenience")
				else:
					query="INSERT INTO FLIGHTS (ORIGIN,DESTINATION,DEPART,ADULT,CHILD,CLASS) VALUES (%s,%s,%s,%s,%s,%s)"
					values=(self.origin_entry.get(),self.destination_entry.get(),self.depart_entry.get(),self.adult_entry.get(),self.child_entry.get(),self.class_combo1.get())
					cur.execute(query,values)
					con.commit()
					search()
			else:
				query="SELECT * FROM DETAILS WHERE ORIGIN ='{}' AND DESTINATION ='{}'".format(self.origin_entry.get(),self.destination_entry.get())
				cur.execute(query)
				result=cur.fetchall()
				if cur.rowcount==0: 
					messagebox.showwarning("Warning", "Sorry , for the inconvenience")
				else:
					query="INSERT INTO FLIGHTS (ORIGIN,DESTINATION,DEPART,RETURN_D,ADULT,CHILD,CLASS) VALUES (%s,%s,%s,%s,%s,%s,%s)"
					values=(self.origin_entry.get(),self.destination_entry.get(),self.depart_entry.get(),self.return_entry.get(),self.adult_entry.get(),self.child_entry.get(),self.class_combo1.get())
					cur.execute(query,values)
					con.commit()
					seat=int(self.child_entry.get())+int(self.adult_entry.get())
					search()

		self.submit=Button(Mainframe,text="SUBMIT",font=('Helvetica',18),width=10,command=submit,bg="#00FFFF").place(x=200,y=395)
		
		


if __name__=="__main__":
	root=Tk()
	application=FLIGHT(root)
	root.mainloop()
