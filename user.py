from tkinter import *
from tkinter import messagebox,ttk
from PIL import Image,ImageTk
import math,random
import pymysql
from datetime import date
from prettytable import PrettyTable

class Bill_App:
    def __init__(self,root,id):
        self.root=root
        self.root.geometry("1600x800+0+0")
        self.root.title("Inventory Management")
        title=Label(self.root,text="Inventory Management System",bd=5,relief=GROOVE,fg="white",bg="red2",font=("times new roman",40,"bold"))
        title.pack(side=TOP,fill=X)
        self.bg= ImageTk.PhotoImage(Image.open("../IMS/icons/bg.jpg"))
        bg= Label(self.root,image=self.bg)
        bg.place(x=0,y=72,relwidth=1,relheight=1)
        self.inventory_b=ImageTk.PhotoImage(file="../IMS/icons/inventory.png")
        self.contact_b=ImageTk.PhotoImage(file="../IMS/icons/contact.png")
        self.exit_b=ImageTk.PhotoImage(file="../IMS/icons/exit.png")
        self.add_b=ImageTk.PhotoImage(file="../IMS/icons/cart.png")
        self.total_entry=DoubleVar()
        self.tax_entry=DoubleVar()
        self.grand_total=DoubleVar()
        self.customer_pay=DoubleVar()
        self.search_item_no=StringVar()
        self.search_item_no.set("")
        self.item_no=StringVar()
        self.item_name=StringVar()
        self.item_price=IntVar()
        con=pymysql.connect(host="localhost",user="root",password="root",database="ims")
        cur=con.cursor()
        cur.execute("SELECT * FROM users WHERE username=%s",(id))
        rows=cur.fetchall()
        for row in rows:
            fn=row[1]
            ln=row[2]
            name=f'{fn} {ln}'
            con.commit()
        con.close()
        self.c_name=StringVar()
        self.c_name.set(name)
        self.username=StringVar()
        self.bill_no=IntVar()
        self.search_bill=StringVar()
        self.username.set(id)
        self.bill_no.set(int(random.randint(1000,9999)))
        
        F1=LabelFrame(self.root,bd=5,relief=GROOVE, text="Customer Details",font=("times new roman",15,"bold"),fg="Black",bg="white")
        F1.place(x=0,y=75,relwidth=1,height=85)
        cname_lbl=Label(F1,bg="red2",fg="white",text="Customer Name:",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=2)
        cname_txt=Entry(F1,textvariable=self.c_name,width=20,font="arial 15",bd=3,relief=SUNKEN,state=DISABLED).grid(row=0,column=1,pady=2,padx=10)
        uname_lbl=Label(F1,bg="red2",fg="white",text="Username:",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        uname_txt=Entry(F1,textvariable=self.username,width=20,font="arial 15",bd=3,relief=SUNKEN,state=DISABLED).grid(row=0,column=3,pady=2,padx=10)
        bill_btn=Button(F1,text="Past orders",command=self.show_bills,bg="red2",fg="white",bd=3,font =("Times New Roman",20,"bold"))
        bill_btn.place(x=900,y=0,width=150,height=45)
        contact_btn=Button(F1,image=self.contact_b,command=self.contact,compound=TOP,pady=6,bg="red2",bd=3).place(x=1390,y=0,width=45,height=45)
        Exit_btn=Button(F1,image=self.exit_b,command=self.exit,width=80,height=65,compound=TOP,pady=6,bg="red2",bd=3).place(x=1450,y=0,width=45,height=45)

        F2=LabelFrame(self.root,bd=5,relief=GROOVE, text="Search Items",font=("times new roman",15,"bold"),fg="Black",bg="white")
        F2.place(x=20,y=170,width=310,height=460)
        self.search_name= StringVar()
        item_no_lbl=Label(F2,text="Item Name.",font=("times new roman",16,"bold"),bg="red2",fg="white").grid(row=0,column=0,padx=0,pady=10,sticky="w")
        combo_search=ttk.Combobox(F2,textvariable=self.search_name,width=15 ,font=("times new roman",13,"bold"),state="readonly")
        combo_search['values']=self.combo_value()
        combo_search.grid(row=0,column=1, padx=20,pady=10)
        combo_search.bind("<<ComboboxSelected>>",self.search_item)
        btn_inventory=Button(F2,image=self.inventory_b,command=self.Inventory_list,width=80,height=65,font=("Arial",7,"bold"),compound=TOP,pady=6,bg="red2",fg="black",bd=3).place(x=20,y=60,width=50,height=50)

        F3=LabelFrame(self.root,bd=5,relief=GROOVE, text="Item Details",font=("times new roman",15,"bold"),fg="Black",bg="white")
        F3.place(x=350,y=170,width=350,height=460)
        prod_id_lbl=Label(F3,text="Item No:",font=("times new roman",16,"bold"),bg="red2",fg="white").grid(row=0,column=0,padx=0,pady=10,sticky="w")
        prod_id_txt=Label(F3,textvariable=self.item_no,font=("times new roman",16,"bold"),width=15,bg="Lightgray",fg="black").grid(row=0,column=1,padx=10,pady=10,stick="w")
        prod_name_lbl=Label(F3,text="Item Name:",font=("times new roman",16,"bold"),bg="red2",fg="white").grid(row=1,column=0,padx=0,pady=10,sticky="w")
        prod_name_txt=Label(F3,textvariable=self.item_name,font=("times new roman",16,"bold"),width=15,bg="Lightgray",fg="black").grid(row=1,column=1,padx=10,pady=10,stick="w")
        prod_price_lbl=Label(F3,text="Price (in Rs):",font=("times new roman",16,"bold"),bg="red2",fg="white").grid(row=2,column=0,padx=0,pady=10,sticky="w")
        prod_price_txt=Label(F3,textvariable=self.item_price,font=("times new roman",16,"bold"),width=15,bg="Lightgray",fg="black").grid(row=2,column=1,padx=10,pady=10,stick="w")
        qty_lbl=Label(F3,text="Item Quantity.",font=("times new roman",16,"bold"),bg="red2",fg="white").grid(row=3,column=0,padx=0,pady=10,sticky="w")
        self.item_quantity=Spinbox(F3, from_=1, to=50,font =("Arial",16),width=5)
        self.item_quantity.grid(row=3,column=1,padx=10,pady=10)
        addcart=Button(F3,image=self.add_b,command=self.add_item,bg="red2",fg="white",pady=15,width=120,bd=3,font="arial 15 bold").grid(row=4,column=1,padx=5,pady=5)

        F4=LabelFrame(self.root,bd=5,relief=GROOVE, text="Shopping Cart",font=("times new roman",16,"bold"),fg="Black",bg="White")
        F4.place(x=720,y=170,width=340,height=460)
        scroll_x=Scrollbar(F4,orient=HORIZONTAL)
        scroll_y=Scrollbar(F4,orient=VERTICAL)
        self.cart_table=ttk.Treeview(F4, column=("1","2","3","4"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.cart_table.xview)
        scroll_y.config(command=self.cart_table.yview)
        self.cart_table.heading("1",text="No.")
        self.cart_table.heading("2",text="Item Name")
        self.cart_table.heading("3",text="Qty")
        self.cart_table.heading("4",text="Price")
        self.cart_table['show']='headings'
        self.cart_table.column("1",width=30)
        self.cart_table.column("2",width=140)
        self.cart_table.column("3",width=10)
        self.cart_table.column("4",width=20)
        self.cart_table.pack(fill=BOTH,expand=1)
        self.cart_table.bind("<ButtonRelease-1>",self.carttable_click)
        style = ttk.Style()
        style.configure("Treeview", highlightthickness=0, bd=0, font=("Arial", 12))
        style.configure("Treeview.Heading", font=("Times new roman", 12, "bold"))
        
        F7=LabelFrame(self.root,bd=5,relief=GROOVE,text="    ",font=("times new roman",16,"bold"),fg="Black",bg="White")
        F7.place(x=1060,y=170,width=60,height=460)
        scrollx=Scrollbar(F7,orient=HORIZONTAL)
        scrolly=Scrollbar(F7,orient=VERTICAL)
        self.delete=ttk.Treeview(F7, column=("1"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.delete.xview)
        scrolly.config(command=self.delete.yview)
        self.delete.heading("1",text="")
        self.delete['show']='headings'
        self.delete.column("1",width=50)
        self.delete.pack(fill=BOTH,expand=1)
        self.delete.bind("<ButtonRelease-1>",self.deletetable_click)

        F5=LabelFrame(self.root,bd=5,relief=GROOVE)
        F5.place(x=1140,y=170,width=370,height=460)
        bill_title=Label(F5,text="Bill Area",font=("arial",15, "bold"), bd=3, bg="red2", relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        F6=LabelFrame(self.root,bd=5,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),bg="White",fg="Black")
        F6.place(x=0,y=640,relwidth=1,height=140)
        Totallbl = Label(F6,text="Total Bill:", font=("Times",14,"bold"),bg="red2",fg="white")
        Totallbl.grid(row=0,column=0,padx=10,pady=5,sticky="w")
        TotalEntry = Entry(F6,width=10, textvariable= self.total_entry,font=("Times",14,"bold"), bd=3, relief=SUNKEN,state=DISABLED)
        TotalEntry.grid(row=0,column=1,padx=10,pady=5)
        GSTlbl = Label(F6,text="GST:", font=("Times",14,"bold"),bg="red2",fg="white")
        GSTlbl.grid(row=1,column=0,padx=10,pady=5,sticky="w")
        GSTEntry = Entry(F6,width=10,textvariable=self.tax_entry,font=("Times",14,"bold"), bd=3, relief=SUNKEN,state=DISABLED)
        GSTEntry.grid(row=1,column=1,padx=10,pady=5)
        GrandTotallbl = Label(F6,text="Grand Total:", font=("Times",14,"bold"),bg="red2",fg="white")
        GrandTotallbl.grid(row=0,column=2,padx=10,pady=5,sticky="w")
        GrandTotalEntry = Entry(F6,width=10,textvariable=self.grand_total,font=("Times",14,"bold"), bd=3, relief=SUNKEN,state=DISABLED)
        GrandTotalEntry.grid(row=0,column=3,padx=10,pady=5)
        CPaylbl = Label(F6,text="Customer Pay:", font=("Times",14,"bold"),bg="red2",fg="white")
        CPaylbl.grid(row=1,column=2,padx=10,pady=5,sticky="w")
        CPayEntry = Entry(F6,width=10, font=("Times",14,"bold"),textvariable=self.customer_pay,bd=3, relief=SUNKEN,state=DISABLED)
        CPayEntry.grid(row=1,column=3,padx=10,pady=5)
        total_btn=Button(F6,text="Total",bg="red2",fg="white",font =("Times New Roman",18,"bold"),command=self.total,bd=3)
        total_btn.place(x=730,y=10,width=100,height=45)
        GBill_btn=Button(F6,text="Generate Bill",bg="red2",fg="white",font =("Times New Roman",18,"bold"),command=self.payment,bd=3)
        GBill_btn.place(x=840,y=10,width=150,height=45)
        Clear_btn=Button(F6,text="Clear",bg="red2",fg="white",font =("Times New Roman",18,"bold"),command=self.clear,bd=3)
        Clear_btn.place(x=1000,y=10,width=100,height=45)
        self.welcome_bill()

    def search_item(self,ev):
        con=pymysql.connect(host="localhost",user="root",password="root",database="ims")
        cur=con.cursor()
        cur.execute(f"SELECT * FROM inventory WHERE product_name='{self.search_name.get()}'")
        rows=cur.fetchall()
        if len(rows)==0:
            messagebox.showinfo("Alert","Choose an item!")
        else:
            for row in rows:
                self.item_no.set(row[0])
                self.item_name.set(row[1])
                self.item_price.set(row[3])
        con.commit()
        con.close()

    def add_item(self):
        if(self.item_no.get()==""):
            messagebox.showinfo("Alert","Choose an item.")
        else:
            con=pymysql.connect(host="localhost",user="root",password="root",database="ims")
            cur=con.cursor()
            cur.execute(f"SELECT * from inventory where product_name='{self.search_name.get()}'")
            rows=cur.fetchall()
            available_quantity=rows[0][2]
            quantity=0
            cart_list=self.cart_table.get_children()
            
            for x in cart_list:
                if str(self.item_name.get())==str(self.cart_table.item(x)['values'][1]):
                    quantity=int(self.cart_table.item(x)['values'][2])
                    self.cart_table.detach(x)
                    self.delete.detach(x)
            q=int(self.item_quantity.get())+quantity
            if q<available_quantity or q==available_quantity:
                new_item=(self.item_no.get(),self.item_name.get(),q,self.item_price.get()*q)
                self.cart_table.insert('',END, values=new_item)
                self.delete.insert('',END,open=True, values=("❌"))
            else:
                messagebox.showinfo("Alert","Available quantity is less.")
                if quantity>0:
                    new_item=(self.item_no.get(),self.item_name.get(),quantity,self.item_price.get()*quantity)
                    self.cart_table.insert('',END, values=new_item)
                    self.delete.insert('',END,open=True, values=("❌"))
            self.total()
            con.close()        
        
    def payment(self):
        cart_list=self.cart_table.get_children()
        i=0
        for x in cart_list:
            i=i+1
        if i==0:
            messagebox.showinfo("Alert","Add items to cart!")
        else:
            self.root4 = Toplevel()
            self.root4.title("Inventory Management")
            self.root4.geometry("750x400+375+200")
            self.cardno = StringVar()
            self.cardname = StringVar()
            self.exp_month = StringVar()
            self.exp_year = StringVar()
            self.cvv_no = StringVar()
            bg1= Label(self.root4,image=self.bg)
            bg1.place(x=0,y=0,relwidth=1,relheight=1)
            title2=Label(self.root4,text="Online Payment",bd=5,relief=GROOVE,fg="white",bg="red2",font=("times new roman",30,"bold"))
            title2.pack(side=TOP,fill=X)
            self.checkout_frame = LabelFrame(self.root4, text="Online Payment", bg = "white", font =("Times New Roman",20))
            self.checkout_frame.place(x = 55, y =80 , height = 300, width = 630)
            card_no = Label(self.checkout_frame, text = " Card No.   : ",bg = "tomato", font =("Times New Roman",16)).grid(row = 0, column = 0,padx = 10, pady = 15,sticky="w")
            self.card_noen = Entry(self.checkout_frame, textvariable = self.cardno,bd=3,width = 27,bg = "LightGray", font =("Times New Roman",16))
            self.card_noen.grid(row = 0, column = 1,padx = 10, pady = 15,sticky="w")
            self.card_noen.bind("<KeyPress>",self.card_no)
            card_name = Label(self.checkout_frame, text = " Name on Card : ",bg = "tomato", font =("Times New Roman",16)).grid(row = 1, column = 0,padx = 10, pady = 15,sticky="w")
            self.card_nameen = Entry(self.checkout_frame, textvariable = self.cardname,bd=3,width = 27,bg = "LightGray", font =("Times New Roman",16))
            self.card_nameen.grid(row = 1, column = 1,columnspan=4,padx = 10, pady = 15,sticky="w")
            self.card_nameen.bind("<KeyPress>",self.card_name)
            exp_date = Label(self.checkout_frame, text = " Expiry Date : ",bg = "tomato", font =("Times New Roman",16)).grid(row = 2, column = 0,padx = 10, pady = 15,sticky="w")
            self.month = ttk.Combobox(self.checkout_frame,textvariable = self.exp_month, font =("Times New Roman",16), width = 5,state = "readonly" , justify = "center")
            self.month['values']=("Jan","Feb","March","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec")
            self.month.grid(row = 2, column = 1, pady = 15,sticky="w")
            self.month.current(0)
            self.year = ttk.Combobox(self.checkout_frame,textvariable = self.exp_year, font =("Times New Roman",16),state = "readonly" , justify = "center")
            self.year['values']=("2021","2022","2022","2023","2024")
            self.year.place(x=250,y=136,width=80,height=30)
            self.year.current(0)
            cvv= Label(self.checkout_frame, text = " CVV : ",bg = "tomato", font =("Times New Roman",18)).place(x=360,y=136,width=80,height=30)
            self.cvv_en = Entry(self.checkout_frame, textvariable = self.cvv_no,bd=3,width = 5,bg = "LightGray", font =("Times New Roman",18))
            self.cvv_en.place(x=460,y=136,width=80,height=30)
            self.cvv_en.bind("<KeyPress>", self.cvv)
            pay_btn=Button(self.checkout_frame,command=self.generate_bill,bg="red2",text="Confirm",fg="white",font =("Times New Roman",18,"bold"),bd=3)
            pay_btn.place(x=250,y=200,width=120,height=40)
    
    def generate_bill(self):
        if self.card_noen.get() =="" or self.card_nameen.get()=="" or self.cvv_en.get()=="":
            messagebox.showerror("Error","All fields are mandatory",parent = self.root4)
        elif len(self.card_noen.get())<19:
            messagebox.showerror("Error","Invalid card number!",parent = self.root4)
        elif len(self.cvv_en.get())<3:
            messagebox.showerror("Error","Invalid CVV!",parent = self.root4)
        else:
            mes= messagebox.askyesno("Notification","Are you sure to proceed?")    
            if mes > 0:
                self.root4.destroy()
                cart_list=self.cart_table.get_children()
                con=pymysql.connect(host="localhost",user="root",password="root",database="ims")
                cur=con.cursor()
                items=""
                ptable=PrettyTable(["S. No.","Product","Qty","Price"])
                self.total()
                i=1
                for x in cart_list:
                    if items!="":
                        items=items+","
                    items=items+str(self.cart_table.item(x)['values'][1])+"("+str(self.cart_table.item(x)['values'][2])+")"
                    statement=f"UPDATE inventory SET product_qty=product_qty-{self.cart_table.item(x)['values'][2]},sales=sales+{self.cart_table.item(x)['values'][2]} WHERE product_id={self.cart_table.item(x)['values'][0]}"
                    cur.execute(statement)
                    con.commit()
                    ptable.add_row([i,self.cart_table.item(x)['values'][1],self.cart_table.item(x)['values'][2],self.cart_table.item(x)['values'][3]])
                    self.cart_table.detach(x)
                    i=i+1
                self.txtarea.insert(END,ptable)
                self.txtarea.insert(END,f"\n=======================================")
                self.txtarea.insert(END,f"\n\t     Subtotal Rs. {self.total_entry.get()}")
                self.txtarea.insert(END,f"\n\t     Sales Tax Rs. {0.18*int(self.total_entry.get())}")
                self.txtarea.insert(END,"\n---------------------------------------")
                self.txtarea.insert(END,"\n------------AFTER DISCOUNT-------------")
                self.txtarea.insert(END,f"\n\t\tTotal Rs.  {self.customer_pay.get()}")
                self.txtarea.insert(END,"\n---------------------------------------")
                self.txtarea.insert(END,"\n\n\n\n\n----------Thanks for Shopping!---------")
                self.bill_data=self.txtarea.get('1.0',END)
                f=open("../IMS/Bill"+str(self.bill_no.get())+".txt","w")
                f.write(self.bill_data)
                f.close()
                messagebox.showinfo("Saved",f"Bill No. :{(self.bill_no.get())} saved Successfully.")
                amount=self.customer_pay.get()
                cur.execute("INSERT INTO sales_bill VALUES(%s,%s,%s,%s,%s)",(self.bill_no.get(),self.username.get(),items,date.today().strftime("%d/%m/%Y"),amount))
                con.commit()
                con.close()
                self.welcome_bill()
                self.clear()

    def total(self):
        ftotal=0
        cart_list=self.cart_table.get_children()
        for x in cart_list:
            ftotal=ftotal+int(self.cart_table.item(x)['values'][3])
        tax = 0.18*ftotal
        gtotal = ftotal + tax
        cust=gtotal-0.02*gtotal
        self.total_entry.set(ftotal)
        self.tax_entry.set(format(tax, ".2f"))
        self.grand_total.set(gtotal)
        self.customer_pay.set(format(cust, ".2f"))

    def welcome_bill(self):
        today=date.today().strftime("%d/%m/%Y")
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome to My Shop")
        self.txtarea.insert(END,f"\n Bill Number: {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name: {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Date: {today}\n")

    def carttable_click(self,ev):
        cursor_row=self.cart_table.focus()
        contents=self.cart_table.item(cursor_row)
        row=contents['values']
        self.item_no.set(row[0])
        self.item_name.set(row[1])
        self.item_quantity.delete(0,"end")
        self.item_quantity.insert(0,1)
        self.item_price.set(int(row[3]/row[2]))
        def choose_qty():
            q=int(spinbox.get())
            con=pymysql.connect(host="localhost",user="root",password="root",database="ims")
            cur=con.cursor()
            cur.execute(f"SELECT * from inventory where product_name='{self.item_name.get()}'")
            rows=cur.fetchall()
            available_quantity=rows[0][2]
            if available_quantity==0:
                messagebox.showinfo("Alert","Out of stock!")
            elif q<available_quantity or q==available_quantity:
                new_item=(self.item_no.get(),self.item_name.get(),q,rows[0][3]*q)
                self.cart_table.detach(cursor_row)
                self.delete.detach(cursor_row)
                self.cart_table.insert('',END, values=new_item)
                self.delete.insert('',END,open=True, values=("❌"))
            else:
                messagebox.showinfo("Alert","Available stock is less.")
            con.close()
            win.destroy()
            self.total()
        win= Tk()
        win.title("Quantity")
        win.geometry("400x190+350+200")
        self.pname=StringVar()
        q=row[2]
        label1=Label(win, text = "Product:", font =("Arial",16),bg="red2", fg="White").place(x=10,y=30,width=120,height=35)
        label2=Label(win, text = "Quantity: ", font =("Arial",16),bg="red2", fg="White").place(x=10,y=80,width=120,height=35)
        product_en=Label(win, text = row[1], font =("Arial",16),fg="black")
        product_en.place(x=140,y=30,width=200,height=35)
        spinbox = Spinbox(win, from_=1, to=50,font =("Arial",16))
        spinbox.place(x=200,y=80,width=50,height=35)
        spinbox.delete(0,"end")
        spinbox.insert(0,q)
        button= Button(win, text= "Done", command= choose_qty,font =("Times New Roman",16,"bold"),bd=3,bg="red2",fg="white")
        button.place(x=150,y=130,width=100,height=35)
        win.mainloop()

    def deletetable_click(self,ev):
        cursor_row=self.delete.focus()
        mes= messagebox.askyesno("Notification","Do You want to remove?")    
        if mes > 0:
            self.delete.detach(cursor_row)
            self.cart_table.detach(cursor_row)
        self.total()
    
    def clear(self):
        self.cart_table.delete(*self.cart_table.get_children())
        self.delete.delete(*self.delete.get_children())
        self.item_no.set("")
        self.item_name.set("")
        self.item_price.set(0)
        self.item_quantity.delete(0,"end")
        self.item_quantity.insert(0,1)
        self.bill_no.set(int(random.randint(1000,9999)))
        self.total_entry.set("")
        self.tax_entry.set("")
        self.grand_total.set("")
        self.customer_pay.set("")
        self.welcome_bill()

    def show_bills(self):
        self.root3=Toplevel()
        self.root3.geometry("720x420")
        self.table_frame=Frame(self.root3,bd=4,relief=RIDGE,bg="ivory")
        self.table_frame.place(x=10,y=10,width=700,height=400)
        scroll_x=Scrollbar(self.table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(self.table_frame,orient=VERTICAL)
        self.billtable=ttk.Treeview(self.table_frame,columns=("1","2","3","4"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.billtable.xview)
        scroll_y.config(command=self.billtable.yview)
        self.billtable.heading("1",text="Bill No.")
        self.billtable.heading("2",text="Items")
        self.billtable.heading("3",text="Date")
        self.billtable.heading("4",text="Amount")
        self.billtable['show']='headings'
        self.billtable.column("1",width=30)
        self.billtable.column("2",width=200)
        self.billtable.column("3",width=50)
        self.billtable.column("4",width=30)
        self.billtable.pack(fill=BOTH,expand=1)
        style = ttk.Style()
        style.configure("Treeview", highlightthickness=0, bd=0, font=("Arial", 12))
        style.configure("Treeview.Heading", font=("Times new roman", 14, "bold"))
        con=pymysql.connect(host="localhost",user="root",password="root",database="ims")
        cur=con.cursor()
        cur.execute("SELECT bill_no,items,date,amount FROM sales_bill WHERE username=%s",self.username.get())
        rows=cur.fetchall()
        if len(rows)!=0:
            self.billtable.delete(*self.billtable.get_children())
            for row in rows:
                self.billtable.insert('',END,values=row)
                con.commit()
        con.close()    
    
    def Inventory_list(self):
        self.root2=Toplevel()
        self.root2.geometry("480x470+10+200")
        self.table_frame=Frame(self.root2,bd=4,relief=RIDGE,bg="ivory")
        self.table_frame.place(x=10,y=10,width=460,height=460)
        scroll_x=Scrollbar(self.table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(self.table_frame,orient=VERTICAL)
        self.invent_table=ttk.Treeview(self.table_frame,columns=("1","2","3"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.invent_table.xview)
        scroll_y.config(command=self.invent_table.yview)
        self.invent_table.heading("1",text="ID")
        self.invent_table.heading("2",text="PRODUCT NAME")
        self.invent_table.heading("3",text="PRICE")
        self.invent_table['show']='headings'
        self.invent_table.column("1",width=10)
        self.invent_table.column("2",width=200)
        self.invent_table.column("3",width=30)
        self.invent_table.pack(fill=BOTH,expand=1)
        self.invent_table.bind("<ButtonRelease-1>",self.inventory_click)
        style = ttk.Style()
        style.configure("Treeview", highlightthickness=0, bd=0, font=("Arial", 12))
        style.configure("Treeview.Heading", font=("Times new roman", 14, "bold"))
        self.data()

    def data(self): 
        con=pymysql.connect(host="localhost",user="root",password="root",database="ims")
        cur=con.cursor()
        cur.execute("SELECT product_id,product_name,product_price from inventory ORDER BY product_id ASC")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.invent_table.delete(*self.invent_table.get_children())
            for row in rows:
                self.invent_table.insert('',END,values=row)
                con.commit()
        con.close()

    def inventory_click(self,ev):
        cursor_row=self.invent_table.focus()
        content=self.invent_table.item(cursor_row)
        row=content['values']
        self.item_no.set(row[0])
        self.item_name.set(row[1])
        self.item_quantity.delete(0,"end")
        self.item_quantity.insert(0,1)
        self.item_price.set(row[2])

    def combo_value(self):
        con=pymysql.connect(host="localhost",user="root",password="root",database="ims")
        cur=con.cursor()
        cur.execute("SELECT product_name from inventory")
        result = []
        for row in cur.fetchall():
            result.append(row[0])
        return result

    def contact(self):
        self.root3=Toplevel()
        self.root3.geometry("450x200+950+160")
        title=Label(self.root3,text="Contact Us",bd=3,relief=GROOVE,fg="white",bg="red2",font=("times new roman",20,"bold"))
        title.pack(side=TOP,fill=X)
        self.txtarea=Text(self.root3,font=("times new roman",16))
        self.txtarea.pack(fill=BOTH,expand=1)
        self.txtarea.insert(END,"\n\t\tIMS STORE\n 12, Near Ulhasnagar, M.G.H road, Mumbai-400 027")
        self.txtarea.insert(END,"\n\t             www.myims.com")
        self.txtarea.insert(END,"\n\t    Email: imsstore@gmail.com")
        self.txtarea.insert(END,"\n       Contact Number. 9942510320,7014299815")
        self.txtarea.pack()
    
    def card_no(self,event):
        if event.keysym == 'Tab':
            return
        if event.keysym == 'Delete':
            return
        if event.keysym == 'BackSpace':
            return
        widget = event.widget  
        entry = widget.get()
        x = widget.index(INSERT)
        if not event.char.isdigit() or x > 18:
            widget.bell()
            return 'break'
        else: 
            widget.delete(x)
        if x==4 or x==9 or x==14:
             event.widget.insert(x, "-")

    
    def card_name(self,event):
        widget = event.widget  
        entry = widget.get()
        x = widget.index(INSERT)
        if event.char.isdigit():
            widget.bell()
            return 'break'
        else:
            widget.delete(x)
    
    def cvv(self,event):
        if event.keysym == 'Delete':
            return
        if event.keysym == 'BackSpace':
            return
        widget = event.widget  
        entry = widget.get()
        x = widget.index(INSERT)
        if not event.char.isdigit() or x > 2:
            widget.bell()
            return 'break'
        else: 
            widget.delete(x)
    
    def exit(self):
        mes= messagebox.askyesno("Notification","Do You want to logout?")    
        if mes > 0:
            self.root.destroy()
            import login

def run_user(id):
    root=Tk()
    obb=Bill_App(root,id)
    root.mainloop()

    