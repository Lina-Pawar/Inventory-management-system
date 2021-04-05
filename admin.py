from tkinter import *
from tkinter import ttk
from matplotlib import pyplot as plt
import pymysql
from tkinter import messagebox
from PIL import Image,ImageTk
import math,random
import os
import datetime
from datetime import date,timedelta
from tkcalendar import Calendar,DateEntry

class Customer:
    def __init__(self,root,id):
        self.root = root
        self.root.title("Inventory Management")
        self.root.geometry("1600x800+0+0")
        title=Label(self.root,text="Inventory Management System",bd=5,relief=GROOVE,fg="white",bg="red2",font=("times new roman",40,"bold"))
        title.pack(side=TOP,fill=X)
        self.bg= ImageTk.PhotoImage(Image.open("../IMS/icons/bg.jpg"))
        bg= Label(self.root,image=self.bg)
        bg.place(x=0,y=72,relwidth=1,relheight=1)
        self.product_id=StringVar()
        self.product_name=StringVar()
        self.product_qty=IntVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()
        self.product_price=IntVar()
        self.threshold=IntVar()
        self.user_id = StringVar()
        self.product_id.set(str(random.randint(1000,9999)))
        
        self.manage_frame=Frame(self.root,bd=5,relief=RIDGE,bg="white")
        self.manage_frame.place(x=30,y=100,width=600,height=650)
        m_title=Label(self.manage_frame,text="PRODUCT MANAGEMENT",bg="red2",fg="white",font=("times new roman",20,"bold"))
        m_title.place(x=0,y=0,width=592,height=50)
        Label(self.manage_frame,text="",bg="red2",fg="red2",font=("times new roman",16,"bold")).grid(row=0,column=0,pady=10,padx=20,sticky="w")
        self.txt_id=Entry(self.manage_frame,textvariable=self.user_id,font=("times new roman",16,"bold"),bd=5,relief=GROOVE,state=DISABLED)
        self.user_id.set(id)
        self.txt_id.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        lbl_id=Label(self.manage_frame,text="PRODUCT ID :",bg="white",fg="black",font=("times new roman",16,"bold"))
        lbl_id.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        self.txt_id=Entry(self.manage_frame,textvariable=self.product_id,font=("times new roman",16,"bold"),bd=5,relief=GROOVE)
        self.txt_id.grid(row=2,column=1,pady=10,padx=20,sticky="w")
        lbl_name=Label(self.manage_frame,text="PRODUCT NAME :",bg="white",fg="black",font=("times new roman",16,"bold"))
        lbl_name.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        self.txt_name=Entry(self.manage_frame,textvariable=self.product_name,font=("times new roman",16,"bold"),bd=5,relief=GROOVE)
        self.txt_name.grid(row=3,column=1,pady=10,padx=20,sticky="w")
        lbl_qty=Label(self.manage_frame,text="QUANTITY :",bg="white",fg="black",font=("times new roman",16,"bold"))
        lbl_qty.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        self.txt_qty=Entry(self.manage_frame,textvariable=self.product_qty,font=("times new roman",16,"bold"),bd=5,relief=GROOVE)
        self.txt_qty.grid(row=4,column=1,pady=10,padx=20,sticky="w")
        self.txt_qty.bind('<KeyPress>', self.num_validate)
        lbl_price=Label(self.manage_frame,text="PRICE (PER UNIT) :",bg="white",fg="black",font=("times new roman",16,"bold"))
        lbl_price.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        self.txt_price=Entry(self.manage_frame,textvariable=self.product_price,font=("times new roman",16,"bold"),bd=5,relief=GROOVE)
        self.txt_price.grid(row=5,column=1,pady=10,padx=20,sticky="w")
        self.txt_price.bind('<KeyPress>', self.num_validate)
        lbl_thres=Label(self.manage_frame,text="THRESHOLD :",bg="white",fg="black",font=("times new roman",16,"bold"))
        lbl_thres.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        self.txt_threshold=Entry(self.manage_frame,textvariable=self.threshold,font=("times new roman",16,"bold"),bd=5,relief=GROOVE)
        self.txt_threshold.grid(row=6,column=1,pady=10,padx=20,sticky="w")
        self.txt_threshold.bind('<KeyPress>', self.num_validate)
        
        self.exit_b=ImageTk.PhotoImage(file="../IMS/icons/exit.png")
        self.lowstock_b=ImageTk.PhotoImage(file="../IMS/icons/inventory.png")
        self.forecast_b=ImageTk.PhotoImage(file="../IMS/icons/forecast.png")
        self.userdet_b=ImageTk.PhotoImage(file="../IMS/icons/user.png")
        
        self.btns=Frame(self.manage_frame,bd=5,relief=GROOVE,bg="white")
        self.btns.place(x=65,y=400,width=465,height=100)
        add_btn=Button(self.btns,text="Add",bg="red2",fg="white",font =("Times New Roman",18,"bold"),bd=3,command=self.add_product).place(x=10,y=5,width=100,height=45)
        update_btn=Button(self.btns,text="Update",bg="red2",fg="white",font =("Times New Roman",18,"bold"),bd=3,command=self.update_data).place(x=120,y=5,width=100,height=45)
        delete_btn=Button(self.btns,text="Delete",bg="red2",fg="white",font =("Times New Roman",18,"bold"),bd=3,command=self.delete_data).place(x=230,y=5,width=100,height=45)
        clear_btn=Button(self.btns,text="Clear",bg="red2",fg="white",font =("Times New Roman",18,"bold"),bd=3,command=self.clear).place(x=340,y=5,width=100,height=45)
        
        self.btn_frame=Frame(self.manage_frame,bd=5,relief=GROOVE,bg="white")
        self.btn_frame.place(x=65,y=470,width=465)
        Sales_btn=Button(self.btn_frame,image=self.lowstock_b,command=self.low_stock,width=40,height=40,bg="red2",bd=3).grid(row=0,column=0,padx=10,pady=5)
        Sales_lbl=Label(self.btn_frame,text="Low stock",bg="white",fg="black",font=("times new roman",12,"bold")).grid(row=1,column=0,padx=10,pady=0)
        forecast_btn= Button(self.btn_frame,image=self.forecast_b, width = 40, height= 40, bg="red2", bd=3, command= self.forecast_prod).grid(row=0, column=1, padx=10, pady= 5)
        forecast_lbl=Label(self.btn_frame,text="Forecasting",bg="white",fg="black",font=("times new roman",12,"bold")).grid(row=1,column=1,padx=10,pady=0)
        userdet_btn=Button(self.btn_frame,image=self.userdet_b,command=self.user_detail,width=40,height=40,bg="red2",bd=3).grid(row=0,column=2,padx=10,pady=5)
        userdet_lbl=Label(self.btn_frame,text="User details",bg="white",fg="black",font=("times new roman",12,"bold")).grid(row=1,column=2,padx=10,pady=0)
        Exit_btn=Button(self.btn_frame,image=self.exit_b,command=self.exit,width=40,height=40,bg="red2",bd=3).grid(row=0,column=3,padx=10,pady=5)
        Exit_lbl=Label(self.btn_frame,text="Logout",bg="white",fg="black",font=("times new roman",12,"bold")).grid(row=1,column=3,padx=10,pady=0)
        
        self.details_frame=Frame(self.root,bd=5,relief=RIDGE,bg="white")
        self.details_frame.place(x=650,y=100,width=850,height=650)
        lbl_search=Label(self.details_frame,text="Type to search...",bg="white",fg="black",font=("times new roman",16,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        self.txt_search=Entry(self.details_frame,width=15,textvariable=self.search_txt,font=("times new roman",16,"bold"),bd=5,relief=GROOVE)
        self.txt_search.grid(row=0,column=1,pady=10,padx=20,sticky="w")
        self.txt_search.bind('<KeyPress>', self.search_data)
        showall_btn=Button(self.details_frame,text="Show all",bg="red2",fg="white",font =("Times New Roman",18,"bold"),bd=3,command=self.fetch_data).place(x=400,y=10,width=120,height=35)
        self.table_frame=Frame(self.details_frame,bd=4,relief=RIDGE,bg="white")
        self.table_frame.place(x=20,y=70,width=800,height=540)
        scroll_x=Scrollbar(self.table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(self.table_frame,orient=VERTICAL)
        self.invent_table=ttk.Treeview(self.table_frame,columns=("00","01","02","03","04","05"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.invent_table.xview)
        scroll_y.config(command=self.invent_table.yview)
        style = ttk.Style()
        style.configure("Treeview", highlightthickness=0, bd=0, font=("Arial", 13))
        style.configure("Treeview.Heading", font=("Times new roman", 15, "bold"))
        self.invent_table.heading("00",text="ID")
        self.invent_table.heading("01",text="PRODUCT NAME")
        self.invent_table.heading("02",text="QUANTITY")
        self.invent_table.heading("03",text="PRICE")
        self.invent_table.heading("04",text="THRESHOLD")
        self.invent_table.heading("05",text="SALES")
        self.invent_table['show']='headings'
        self.invent_table.column("00",width=40)
        self.invent_table.column("01",width=160)
        self.invent_table.column("02",width=70)
        self.invent_table.column("03",width=50)
        self.invent_table.column("04",width=70)
        self.invent_table.column("05",width=40)
        self.invent_table.pack(fill=BOTH,expand=1)
        self.invent_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    
    def exit(self):
        mes= messagebox.askyesno("Notification","Do You want to logout?")    
        if mes > 0:
            self.root.destroy()
            import login
    
    def add_product(self):
        if self.product_id.get()=="" or self.product_name.get()=="":
            messagebox.showerror("Error","All field areas required!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="root",database="ims")
            cur=con.cursor()
            cur.execute("INSERT INTO inventory VALUES(%s,%s,%s,%s,%s,0)",(self.product_id.get(),self.product_name.get(),self.product_qty.get(),self.product_price.get(),self.threshold.get()))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Product added successfully!",parent = self.root)

    def fetch_data(self): 
        self.search_txt.set("")
        con=pymysql.connect(host="localhost",user="root",password="root",database="ims")
        cur=con.cursor()
        cur.execute("SELECT * FROM inventory ORDER BY product_id ASC")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.invent_table.delete(*self.invent_table.get_children())
            for row in rows:
                self.invent_table.insert('',END,values=row)
                con.commit()
        con.close()
        
    def low_stock(self):
        con=pymysql.connect(host="localhost",user="root",password="root",database="ims")
        cur=con.cursor()
        cur.execute("SELECT * from inventory where threshold>product_qty ORDER BY product_qty ASC")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.invent_table.delete(*self.invent_table.get_children())
            for row in rows:
                self.invent_table.insert('',END,values=row)
                con.commit()
        con.close()

    def clear(self):
        self.product_id.set(str(random.randint(1000,9999)))
        self.product_name.set("")
        self.product_qty.set("")  
        self.product_price.set("") 
        self.threshold.set("")

    def get_cursor(self,ev):
        cursor_row=self.invent_table.focus()
        content=self.invent_table.item(cursor_row)
        row=content['values']
        self.product_id.set(row[0])
        self.product_name.set(row[1])
        self.product_qty.set(row[2])
        self.product_price.set(row[3]) 
        self.threshold.set(row[4])
        
    def update_data(self):
        if self.product_name.get()!="" and self.product_qty.get()!="" and self.product_price.get()!="" and self.threshold.get()!="":
            con=pymysql.connect(host="localhost",user="root",password="root",database="ims")
            cur=con.cursor()
            cur.execute("UPDATE inventory SET product_name=%s,product_qty=%s,product_price=%s,threshold=%s WHERE product_id=%s",(self.product_name.get(),self.product_qty.get(),self.product_price.get(),self.threshold.get(),self.product_id.get()))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
    
    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="root",database="ims")
        cur=con.cursor()
        cur.execute("DELETE FROM inventory WHERE product_id=%s",self.product_id.get())
        con.commit()
        con.close()
        messagebox.showinfo("Success","Product removed!",parent = self.root)
        self.fetch_data()
        self.clear()
    
    def search_data(self,event): 
        con=pymysql.connect(host="localhost",user="root",password="root",database="ims")
        cur=con.cursor()
        statement=("SELECT * FROM inventory WHERE product_id LIKE '%"+self.search_txt.get()+"%' OR product_name LIKE '%"+self.search_txt.get()+"%' ORDER BY product_id ASC")
        cur.execute(statement)
        self.invent_table.delete(*self.invent_table.get_children())
        rows=cur.fetchall()
        if len(rows)!=0:
            self.invent_table.delete(*self.invent_table.get_children())
            for row in rows:
                self.invent_table.insert('',END, values=row)
            con.commit()
        con.close()

    def user_detail(self):
        self.root2 = Toplevel()
        self.root2.title("Inventory Management")
        self.root2.geometry("1600x800+0+0")
        title2=Label(self.root2,text="User Details",bd=5,relief=GROOVE,fg="white",bg="red2",font=("times new roman",40,"bold"))
        title2.pack(side=TOP,fill=X)
        bg1= Label(self.root2,image=self.bg)
        bg1.place(x=0,y=72,relwidth=1,relheight=1)
        self.userdet_frame=Frame(self.root2,bd=5,relief=RIDGE,bg="white")
        self.userdet_frame.place(x=20,y=100,width=750,height=650)
        ud_title=Label(self.userdet_frame,text="USER DETAILS",bg="red2",fg="white",font=("times new roman",20,"bold"))
        ud_title.place(x=0,y=0,width=740,height=50)
        self.table_frame4=Frame(self.userdet_frame,bd=4,relief=RIDGE,bg="white")
        self.table_frame4.place(x=10,y=60,width=720,height=560)
        scroll_x=Scrollbar(self.table_frame4,orient=HORIZONTAL)
        scroll_y=Scrollbar(self.table_frame4,orient=VERTICAL)
        self.udetail_table=ttk.Treeview(self.table_frame4,columns=("00","01","02","03","04","05"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.udetail_table.xview)
        scroll_y.config(command=self.udetail_table.yview)
        style = ttk.Style()
        style.configure("Treeview", highlightthickness=0, bd=0, font=("Arial", 13))
        style.configure("Treeview.Heading", font=("Times new roman", 15, "bold"))
        self.udetail_table.heading("00",text="ID")
        self.udetail_table.heading("01",text="FIRST NAME")
        self.udetail_table.heading("02",text="LAST NAME")
        self.udetail_table.heading("03",text="CONTACT NO.")
        self.udetail_table.heading("04",text="MAIL ID")
        self.udetail_table.heading("05",text="USERNAME")
        self.udetail_table['show']='headings'
        self.udetail_table.column("00",width=20)
        self.udetail_table.column("01",width=130)
        self.udetail_table.column("02",width=130)
        self.udetail_table.column("03",width=85)
        self.udetail_table.column("04",width=100)
        self.udetail_table.column("05",width=110)
        self.udetail_table.pack(fill=BOTH,expand=1)
        self.udetail_table.bind("<ButtonRelease-1>",self.bills)
        self.userdata()
        self.table2_frame=Frame(self.root2,bd=5,relief=RIDGE,bg="white")
        self.table2_frame.place(x=790,y=100,width=720,height=650)
        bd_title=Label(self.table2_frame,text="ORDER DETAILS",bg="red2",fg="white",font=("times new roman",20,"bold"))
        bd_title.place(x=0,y=0,width=710,height=50)
        self.bill_frame=Frame(self.table2_frame,bd=4,relief=RIDGE,bg="ivory")
        self.bill_frame.place(x=10,y=60,width=690,height=560)
        scroll_x=Scrollbar(self.bill_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(self.bill_frame,orient=VERTICAL)
        self.billtable=ttk.Treeview(self.bill_frame,columns=("00","01","02","03"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.billtable.xview)
        scroll_y.config(command=self.billtable.yview)
        self.billtable.heading("00",text="Bill No.")
        self.billtable.heading("01",text="Items")
        self.billtable.heading("02",text="Date")
        self.billtable.heading("03",text="Amount")
        self.billtable['show']='headings'
        self.billtable.column("00",width=30)
        self.billtable.column("01",width=200)
        self.billtable.column("02",width=50)
        self.billtable.column("03",width=30)
        self.billtable.pack(fill=BOTH,expand=1)
        style = ttk.Style()
        style.configure("Treeview", highlightthickness=0, bd=0, font=("Arial", 12))
        style.configure("Treeview.Heading", font=("Times new roman", 14, "bold"))

    def userdata(self):
        con=pymysql.connect(host="localhost",user="root",password="root",database="ims")
        cur=con.cursor()
        cur.execute("SELECT ID,f_name,l_name,contact,mail_id,username FROM users ORDER BY ID ASC")
        rows=cur.fetchall()
        self.udetail_table.delete(*self.udetail_table.get_children())
        if len(rows)!=0:
            for row in rows:
                self.udetail_table.insert('',END,values=row)
                con.commit()
        con.close()

    def bills(self,ev):
        row=self.udetail_table.focus()
        val=self.udetail_table.item(row)
        uname=val['values'][5]
        self.billtable.delete(*self.billtable.get_children())
        con=pymysql.connect(host="localhost",user="root",password="root",database="ims")
        cur=con.cursor()
        cur.execute("SELECT bill_no,items,date,amount FROM sales_bill WHERE username=%s",uname)
        rows=cur.fetchall()
        if len(rows)!=0:
            for row in rows:
                self.billtable.insert('',END,values=row)
                con.commit()
        con.close()

    def forecast_prod(self):
        self.root3 = Toplevel()
        self.root3.title("Inventory Management")
        self.root3.geometry("1600x800+0+0")
        title2=Label(self.root3,text="Forecasting",bd=5,relief=GROOVE,fg="white",bg="red2",font=("times new roman",40,"bold"))
        title2.pack(side=TOP,fill=X)
        bg2= Label(self.root3,image=self.bg)
        bg2.place(x=0,y=72,relwidth=1,relheight=1)
        self.bp=DoubleVar()
        self.sp=DoubleVar()
        self.profit=DoubleVar()
        self.calender1=StringVar()
        self.calender2=StringVar()
        F1=LabelFrame(self.root3,bd=5,relief=GROOVE, text="Sale details",font=("times new roman",15,"bold"),fg="Black",bg="white")
        F1.place(x=10,y=640,width=780,height=150)
        bp_lbl=Label(F1,bg="red2",fg="white",text="Buying price:",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=15,pady=5)
        bp_txt=Entry(F1,textvariable=self.bp,width=20,font="arial 15",bd=3,relief=SUNKEN,state=DISABLED).grid(row=0,column=1,pady=2,padx=10)
        sp_lbl=Label(F1,bg="red2",fg="white",text="  Sales price:  ",font=("times new roman",18,"bold")).grid(row=1,column=0,padx=15,pady=5)
        sp_txt=Entry(F1,textvariable=self.sp,width=20,font="arial 15",bd=3,relief=SUNKEN,state=DISABLED).grid(row=1,column=1,pady=2,padx=10)
        p_lbl=Label(F1,bg="red2",fg="white",text="Profit:",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=15,pady=5)
        p_txt=Entry(F1,textvariable=self.profit,width=20,font="arial 15",bd=3,relief=SUNKEN,state=DISABLED).grid(row=0,column=3,pady=2,padx=10)
        
        calender_btn=Button(self.root3,text="Choose",command=self.calender, font = ("times new roman",18,"bold"),bd=3,bg="red2",fg="White")
        calender_btn.place(x=10,y=590,width=150,height=40)
        cal1=Entry(self.root3,textvariable=self.calender1,width=20,font="arial 15",bd=3,relief=SUNKEN,state=DISABLED)
        cal1.place(x=170,y=590,width=150,height=40)
        cal2=Entry(self.root3,textvariable=self.calender2,width=20,font="arial 15",bd=3,relief=SUNKEN,state=DISABLED)
        cal2.place(x=330,y=590,width=150,height=40)
        sales_btn=Button(self.root3,text="Sales",command=self.month_graph, font = ("times new roman",18,"bold"),bd=3,bg="red2",fg="White")
        sales_btn.place(x=490,y=590,width=100,height=40)
        prod_btn=Button(self.root3,text="Top Products",command=self.product_graph, font = ("times new roman",18,"bold"),bd=3,bg="red2",fg="White")
        prod_btn.place(x=610,y=590,width=150,height=40)
        
        self.forcast_frame=Frame(self.root3,bd=5,relief=RIDGE,bg="white")
        self.forcast_frame.place(x=810,y=100,width=700,height=650)
        bd_title=Label(self.forcast_frame,text="SALE ESTIMATIONS",bg="red2",fg="white",font=("times new roman",20,"bold"))
        bd_title.place(x=0,y=0,width=710,height=50)
        self.forcast_frame=Frame(self.forcast_frame,bd=4,relief=RIDGE,bg="ivory")
        self.forcast_frame.place(x=10,y=60,width=690,height=560)
        scroll_x=Scrollbar(self.forcast_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(self.forcast_frame,orient=VERTICAL)
        self.forcast_table=ttk.Treeview(self.forcast_frame,columns=("00","01","02","03","04"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.forcast_table.xview)
        scroll_y.config(command=self.forcast_table.yview)
        self.forcast_table.heading("00",text="ID")
        self.forcast_table.heading("01",text="Product")
        self.forcast_table.heading("02",text="Overall Sales")
        self.forcast_table.heading("03",text="Monthly")
        self.forcast_table.heading("04",text="Yearly")
        self.forcast_table['show']='headings'
        self.forcast_table.column("00",width=5)
        self.forcast_table.column("01",width=120)
        self.forcast_table.column("02",width=20)
        self.forcast_table.column("03",width=30)
        self.forcast_table.column("04",width=30)
        self.forcast_table.pack(fill=BOTH,expand=1)
        style = ttk.Style()
        style.configure("Treeview", highlightthickness=0, bd=0, font=("Arial", 12))
        style.configure("Treeview.Heading", font=("Times new roman", 14, "bold"))
        self.sale_records()
        self.product_graph()

    def calender(self):
        def get_date():
            self.calender1.set(cal1.selection_get())
            self.calender2.set(cal2.selection_get())
            win.destroy()
        win= Tk()
        win.title("Calendar")
        win.geometry("480x480")
        label1=Label(win, text = "Start date: ", font =("Arial",16),bg="red2", fg="White").place(x=10,y=70,width=120,height=35)
        label2=Label(win, text = "End date: ", font =("Arial",16),bg="red2", fg="White").place(x=10,y=270,width=120,height=35)
        cal1=Calendar(win, font="Arial 9",locale='en_US',selectmode='day', year=2021, month=4, day=1)
        cal1.pack()
        cal2=Calendar(win, font="Arial 9",locale='en_US', selectmode='day', year=2021, month=4, day=1)
        cal2.pack()
        button= Button(win, text= "Done", command= get_date,font =("Times New Roman",16,"bold"),bd=3,bg="red2",fg="white")
        button.place(x=200,y=420,width=100,height=35)
        win.mainloop()
    
    def sale_records(self):
        con=pymysql.connect(host="localhost",user="root",password="root",database="ims")
        cur=con.cursor()
        cur.execute("SELECT * FROM inventory ORDER BY product_id ASC")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.forcast_table.delete(*self.forcast_table.get_children())
            for row in rows:
                if row[5]<=10:
                    monthly=10
                elif row[5]<=20:
                    monthly=20
                elif row[5]<=30:
                    monthly=30
                elif row[5]<=40:
                    monthly=40
                elif row[5]<=50:
                    monthly=50
                elif row[5]<=60:
                    monthly=60
                elif row[5]<=70:
                    monthly=70
                elif row[5]<=80:
                    monthly=80
                elif row[5]<=90:
                    monthly=90
                elif row[5]<=100:
                    monthly=100
                
                vals=(row[0],row[1],row[5],monthly,monthly*12)
                self.forcast_table.insert('',END,values=vals)
            con.commit()
        con.close()
    
    def month_graph(self):
        days=[]
        sales=[]
        self.product=[]
        self.quantity=[]
        end = datetime.datetime.strptime(self.calender2.get(), "%Y-%m-%d").date()
        start = datetime.datetime.strptime(self.calender1.get(), "%Y-%m-%d").date()
        i=int(str((end-start))[:2])
        while i>=0:
            d=(start + timedelta(days = i)).strftime("%d/%m/%Y")
            days.append(d[:5])
            con=pymysql.connect(host="localhost",user="root",password="root",database="ims")
            cur=con.cursor()
            cur.execute("SELECT * FROM sales_bill WHERE date=%s",d)
            rows=cur.fetchall()
            amount=0.0
            for row in rows:
                val=str(row[2])
                s={sub.split("(")[0]: sub.split("(")[1] for sub in val[:-1].split("),")}
                self.product.extend(list(s.keys()))
                self.quantity.extend(list(s.values()))
                amount=amount+float(str(row[4]))
            sales.append(amount)
            con.commit
            con.close
            i=i-1
        days.reverse()
        sales.reverse()
        selling_price=sum(sales)
        self.sp.set(format(selling_price, ".2f"))
        cost_price=0.0
        i=0
        while i<len(self.product):
            con=pymysql.connect(host="localhost",user="root",password="root",database="ims")
            cur=con.cursor()
            cur.execute("SELECT * FROM inventory WHERE product_name=%s",self.product[i])
            row=cur.fetchone()
            cost_price+=int(row[3])*int(self.quantity[i])
            i=i+1
        self.bp.set(cost_price)
        self.profit.set(format(self.sp.get()-self.bp.get(), ".2f"))
        plt.clf()
        plt.plot(days,sales)
        plt.xlabel('Days', fontsize=16)
        plt.ylabel('Sales', fontsize=16)
        fig = plt.gcf()
        fig.suptitle('Sales per Day', fontsize=18)
        fig.set_size_inches(8,5)
        fig.savefig("MGraph.jpg")
        self.sales_graph=ImageTk.PhotoImage(Image.open("../IMS/MGraph.jpg"))
        self.graph.config(image=self.sales_graph)
        os.remove("MGraph.jpg")
    
    def product_graph(self):
        self.fetch_data()
        products=[]
        sales=[]
        l = [(self.invent_table.set(k, 5), k) for k in self.invent_table.get_children('')]
        l.sort(key=lambda t: int(t[0]),reverse=True)
        for index, (val, k) in enumerate(l):
            self.invent_table.move(k, '', index)
        for x in self.invent_table.get_children():
            products.append(self.invent_table.item(x)['values'][1])
            sales.append(self.invent_table.item(x)['values'][5])
        products=products[:5]
        sales=sales[:5]
        plt.clf()
        plt.bar(products,sales)
        plt.xlabel('Products', fontsize=16)
        plt.ylabel('Quantity', fontsize=16)
        fig=plt.gcf()
        fig.suptitle('5 Highest selling products', fontsize=18)
        fig.set_size_inches(8,5)
        fig.savefig("PGraph.jpg")
        self.prod_graph=ImageTk.PhotoImage(Image.open("../IMS/PGraph.jpg"))
        self.graph=Label(self.root3,image=self.prod_graph)
        self.graph.place(x=10,y=80,width=780,height=500)
        os.remove("PGraph.jpg")
        self.fetch_data()
    
    def num_validate(self,event):
        if event.keysym == 'Tab':
            return
        if event.keysym == 'BackSpace':
            return
        widget = event.widget  
        entry = widget.get()
        x = widget.index(INSERT)
        if not event.char.isdigit() or x > 4:
            widget.bell()
            return 'break'
        else: 
            widget.delete(x)  

def run_admin(id):
    root=Tk() 
    obj=Customer(root,id)
    root.mainloop()
