from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import mysql.connector as mycon
from tkinter import messagebox 
from tkinter import filedialog
from datetime import date
from PIL import Image,ImageTk
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

class FLIGHT:
    def __init__(self,root):
      root.title("EMERALD AIRLINES")
      
      frame=Frame(root,bd=20,width=700,height=700,relief=RIDGE,bg="#aedb9f")
      frame.grid()
      
      self.label=Label(frame,text="CANCEL FLIGHT",font=("Arial bold",22),bg="#aedb9f")
      self.label.grid(row=0,column=0,columnspan=1)
      #self.cancel_label=Label(root,text="CANCEL FLIGHTS",font=("Arial bold",18),bg="#aedb9f")
      #self.cancel_label.grid(row=1,column=0,sticky=W)

      self.flight_no_label=Label(frame,text="FLIGHT NO:",font=("Helvetica",15),bg="#aedb9f")
      self.flight_no_label.grid(row=2,column=0)
      self.flight_no_entry=Entry(frame)
      self.flight_no_entry.grid(row=2,column=1,pady=5,padx=15)

      self.name_label=Label(frame,text="NAME :",font=("Helvetica",15),bg="#aedb9f")
      self.name_label.grid(row=3,column=0)
      self.name_entry=Entry(frame)
      self.name_entry.grid(row=3,column=1,pady=5,padx=15)

      self.aad_label=Label(frame,text="AADHAR NO :",font=("Helvetica",15),bg="#aedb9f")
      self.aad_label.grid(row=4,column=0)
      self.aad_entry=Entry(frame)
      self.aad_entry.grid(row=4,column=1,pady=5,padx=15)

      self.origin_label=Label(frame,text="ORIGIN :",font=("Helvetica",15),bg="#aedb9f")
      self.origin_label.grid(row=5,column=0)
      self.origin_entry=Entry(frame)
      self.origin_entry.grid(row=5,column=1,pady=5,padx=15)

      self.destination_label=Label(frame,text="DESTINATION :",font=("Helvetica",15),bg="#aedb9f")
      self.destination_label.grid(row=6,column=0)
      self.destination_entry=Entry(frame)
      self.destination_entry.grid(row=6,column=1,pady=5,padx=15)

      def show():
            con=mycon.connect(host='localhost',user='root',password='password')
            cur=con.cursor()
            cur.execute("CREATE DATABASE IF NOT EXISTS FLIGHT")
            con.commit()
            cur.execute("USE FLIGHT")
            query="SELECT PASSANGERS.FLIGHT_NO,NAME,AADHAR_NO,AGE,GENDER FROM FLIGHTS,PASSANGERS WHERE FLIGHTS.FLIGHT_NO=PASSANGERS.FLIGHT_NO AND FLIGHTS.FLIGHT_NO='{}' AND PASSANGERS.NAME='{}' AND PASSANGERS.AADHAR_NO='{}' AND FLIGHTS.ORIGIN='{}' AND FLIGHTS.DESTINATION='{}'".format(self.flight_no_entry.get(),self.name_entry.get(),self.aad_entry.get(),self.origin_entry.get(),self.destination_entry.get())
            cur.execute(query)
            results=cur.fetchall()
            if cur.rowcount==0:
                  messagebox.showwarning("Warning", "No such record found")
            else:
                  for row in results:
                        self.tree = ttk.Treeview(frame, columns=('FLIGHT NO.','NAME','AADHAR NO','AGE','GENDER'))

                        self.tree.heading('#0', text='S.NO')
                        self.tree.heading('#1', text='FLIGHT NO.')
                        self.tree.heading('#2', text='NAME')
                        self.tree.heading('#3', text='AADHAR NO.')
                        self.tree.heading('#4', text='AGE')
                        self.tree.heading('#5', text='GENDER')

                        self.tree.column('#0', stretch=YES)
                        self.tree.column('#1', stretch=YES)
                        self.tree.column('#2', stretch=YES)
                        self.tree.column('#3', stretch=YES)
                        self.tree.column('#4', stretch=YES)
                        self.tree.column('#5', stretch=YES)

                        self.tree.grid(row=8, columnspan=3, sticky='nsew')
                        self.treeview = self.tree

                        self.id = 1
                        self.iid = 0

                        self.treeview.insert('', 'end', iid=self.iid,text=str(self.id),
                             values=(self.flight_no_entry.get(),
                                     self.name_entry.get(),row[2],row[3],row[4]))
                        self.iid = self.iid + 1
                        self.id = self.id + 1

                        def cancel():
                              con=mycon.connect(host='localhost',user='root',password='password')
                              cur=con.cursor()
                              cur.execute("CREATE DATABASE IF NOT EXISTS FLIGHT")
                              con.commit()
                              cur.execute("USE FLIGHT")
                              query="DELETE FROM PASSANGERS WHERE FLIGHT_NO='{}' AND NAME='{}' AND AADHAR_NO='{}'".format(self.flight_no_entry.get(),self.name_entry.get(),self.aad_entry.get())
                              cur.execute(query)
                              con.commit()
                              selected_item =self.treeview.selection()[0] ## get selected item
                              self.treeview.delete(selected_item)
                              messagebox.showinfo("Success", "Thank you for chosing EMERALD AIRLINES")
                              self.flight_no_entry.delete(0,END)
                              self.name_entry.delete(0,END)
                              self.origin_entry.delete(0,END)
                              self.destination_entry.delete(0,END)

                        self.cancel_button = Button(frame, text="CONFIRM", command=cancel,bg="#00FFFF")
                        self.cancel_button.grid(row=9, column=2)
                        def exi():
                              root.destroy()
                              exit()
                        self.exi_button = Button(frame, text="EXIT", command=exi,bg="#00FFFF")
                        self.exi_button.grid(row=9, column=1)

      self.submit=Button(frame,text='SUBMIT',font=("Helvetica",16),command=show,bg="#00FFFF")
      self.submit.grid(row=7,column=0,padx=5,pady=15)

      root.mainloop()

root=Tk()
application=FLIGHT(root)
root.mainloop()
