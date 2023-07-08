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
		self.root=root
		self.root.title("EMERALD AIRLINES")
		self.root.geometry("1400x700+0+0")
		self.bg=ImageTk.PhotoImage(file="images/flight1.png")
		bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

		def billing():
			self.root.destroy()
			import gg
		def cancel():
			self.root.destroy()
			import Cancel

		b1=Button(self.root,text="BOOK FLIGHT",relief=SUNKEN,width=20,font=("Helvetica",18),command=billing)
		b1.place(x=1000,y=570)

		b2=Button(self.root,text="CANCEL FLIGHT",relief=SUNKEN,width=20,font=("Helvetica",18),command=cancel)
		b2.place(x=1000,y=620)

root=Tk()
application=FLIGHT(root)
root.mainloop()

