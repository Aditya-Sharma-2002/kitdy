from tkinter import *
from tkinter import ttk
from datetime import date,timedelta #datetime
import datetime
from plyer import notification
import mysql.connector
import time
from tkinter import messagebox

mydb = mysql.connector.connect(host='localhost',user='root',password='',database='kitdy')
mycursor = mydb.cursor()

def graph():
    count = 0
    mycursor.execute("SELECT year(purchased) FROM groceries")
    for i in mycursor.fetchall():
        if int(e17.get()) == int(i[0]):
            count = 1 
    if count == 1:
        from matplotlib import pyplot as plt
        mycursor.execute("SELECT price FROM groceries WHERE year(purchased) ="+ e17.get()+" AND month(purchased) = 1")
        m1 = 0
        for i in mycursor.fetchall():
            m1+=i[0]
        mycursor.execute("SELECT price FROM groceries WHERE year(purchased) ="+ e17.get()+" AND month(purchased) = 2")
        m2 = 0
        for i in mycursor.fetchall():
            m2+=i[0]
        mycursor.execute("SELECT price FROM groceries WHERE year(purchased) ="+ e17.get()+" AND month(purchased) = 3")
        m3 = 0
        for i in mycursor.fetchall():
            m3+=i[0]
        mycursor.execute("SELECT price FROM groceries WHERE year(purchased) = "+ e17.get()+" AND month(purchased) = 4")
        m4 = 0
        for i in mycursor.fetchall():
            m4+=i[0]
        mycursor.execute("SELECT price FROM groceries WHERE year(purchased) ="+ e17.get()+" AND month(purchased) = 5")
        m5 = 0
        for i in mycursor.fetchall():
            m5+=i[0]
        mycursor.execute("SELECT price FROM groceries WHERE year(purchased) ="+ e17.get()+" AND month(purchased) = 6")
        m6 = 0
        for i in mycursor.fetchall():
            m6+=i[0]
        mycursor.execute("SELECT price FROM groceries WHERE year(purchased) ="+ e17.get()+" AND month(purchased) = 7")
        m7 = 0
        for i in mycursor.fetchall():
            m7+=i[0]
        mycursor.execute("SELECT price FROM groceries WHERE year(purchased) ="+ e17.get()+" AND month(purchased) = 8")
        m8 = 0
        for i in mycursor.fetchall():
            m8+=i[0]
        mycursor.execute("SELECT price FROM groceries WHERE year(purchased) ="+ e17.get()+" AND month(purchased) = 9")
        m9 = 0
        for i in mycursor.fetchall():
            m9+=i[0]
        mycursor.execute("SELECT price FROM groceries WHERE year(purchased) ="+ e17.get()+" AND month(purchased) = 10")
        m10 = 0
        for i in mycursor.fetchall():
            m10+=i[0]
        mycursor.execute("SELECT price FROM groceries WHERE year(purchased) ="+ e17.get()+" AND month(purchased) = 11")
        m11 = 0
        for i in mycursor.fetchall():
            m11+=i[0]
        mycursor.execute("SELECT price FROM groceries WHERE year(purchased) ="+ e17.get()+" AND month(purchased) = 12")
        m12 = 0
        for i in mycursor.fetchall():
            m12+=i[0]
        X = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec']
        Y = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
        fig = plt.figure()
        plt.bar(X,Y)
        fig.suptitle("Monthly Expenditure Graph")
        plt.ylabel("Amount")
        plt.show()
    else:
        messagebox.showinfo("Kitdy","No data found")

def examine():
    if len(e1.get()) == 0:
        e1.configure(bg="red")
    else:
        e1.configure(bg="white")
    if e3.get().isdigit() == False:
        e3.configure(bg="red")
    else:
        e3.configure(bg="white")
    if e5.get() < str(d):
        e5.configure(bg="red")
    else:
        e5.configure(bg="white")
    if e6.get() > e5.get():
        e6.configure(bg="red")
    else:
        e6.configure(bg="white")
    if e7.get().isdigit() == False:
        e7.configure(bg="red")
    else:
        e7.configure(bg="white")
    if e8.get() > str(d):
        e8.configure(bg="red")
    else:
        e8.configure(bg="white")

def examine2():
    if len(e10.get()) == 0:
        e10.configure(bg="red")
    else:
        e10.configure(bg="white")
    if e12.get().isdigit() == False:
        e12.configure(bg="red")
    else:
        e12.configure(bg="white")
    if e14.get().isdigit() == False:
        e14.configure(bg="red")
    else:
        e14.configure(bg="white")

def insert():
    examine()
    try:
        import datetime
        dt = datetime.timedelta(7)
        from datetime import datetime,timedelta
        test = datetime.strptime(e5.get(),"%Y-%m-%d").date()
        print(test)
        print(test - dt)
    except ValueError:
        pass

    if e3.get().isdigit and e5.get() > str(d) and e8.get() <= str(d): #and e7.get().isdigit()
        mycursor.execute("ALTER TABLE groceries AUTO_INCREMENT=1")
        mycursor.execute("INSERT INTO groceries(product,brand,quantity,unit,expire,notify,price,purchased) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get()))
        mydb.commit()
    else:
        messagebox.showerror("Kitdy","Please check the data entered is correct or not")

def search():
    for i in table.get_children():
        table.delete(i)
    mycursor.execute("SELECT * FROM groceries WHERE product LIKE '%"+ e9.get() +"%'")
    for i in mycursor.fetchall():
        table.insert('','end',value=i)

def show():
    for i in table.get_children():
        table.delete(i)
    mycursor.execute("SELECT * FROM groceries")
    for i in mycursor.fetchall():
        table.insert('' , 'end', values=i)

def clear():
    var1.set("")
    var2.set("")
    var3.set("")
    var4.set("")
    var5.set("")
    var6.set("")
    var7.set("")
    var8.set("")
    se1.set("")
    e1.configure(bg="white")
    e3.configure(bg="white")
    e5.configure(bg="white")
    e6.configure(bg="white")
    e7.configure(bg="white")
    e8.configure(bg="white")

def clear2():
    var9.set("")
    var10.set("")
    var11.set("")
    var12.set("")
    var13.set("")
    se2.set("")
    e10.configure(bg="white")
    e12.configure(bg="white")
    e14.configure(bg="white")

def cursor(e):
    cursor = table.focus()
    content = table.item(cursor)
    row = content['values']
    se1.set(row[0])
    var1.set(row[1])
    var2.set(row[2])
    var3.set(row[3])
    var4.set(row[4])
    var5.set(row[5])
    var6.set(row[6])
    var7.set(row[7])
    var8.set(row[8])

def cursor2(e):
    cursor = table1.focus()
    content = table1.item(cursor)
    row = content['values']
    se2.set(row[0])
    var9.set(row[1])
    var10.set(row[2])
    var11.set(row[3])
    var12.set(row[4])
    var13.set(row[5])

def update():
    examine()
    if e3.get().isdigit and e5.get() > str(d) and e7.get().isdigit() and e8.get() <= str(d):
        mycursor.execute("UPDATE groceries SET product = %s,brand = %s,quantity = %s,unit = %s,expire = %s,notify = %s,price = %s,purchased = %s WHERE serial = %s",(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e0.get()))
        mydb.commit()
    else:
        messagebox.showerror("Kitdy","Please check the data entered is correct or not")

def update2():
    examine2()
    if len(e10.get()) != 0 and e12.get().isdigit() and len(e13.get()) != 0 and e14.get().isdigit():
        mycursor.execute("UPDATE grocery_list SET product = %s,brand = %s,quantity = %s,unit = %s,price = %s WHERE serial = %s",(e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e16.get()))
        mydb.commit()
    else:
        messagebox.showerror("Kitdy","Please check the data entered is correct or not")

def delete():
    cursor = table.focus()
    content = table.item(cursor)
    row = content['values']
    temp = row[0]
    mycursor.execute("DELETE FROM groceries WHERE serial ="+str(temp))
    mydb.commit()

def grocery():
    hide()
    frame1.pack(fill="both",expand=1)

def buy():
    hide()
    frame2.pack(fill="both",expand=1)

def hide():
    frame1.pack_forget()
    frame2.pack_forget()

def insert2():
    examine2()
    if len(e10.get()) != 0 and e12.get().isdigit() and len(e13.get()) != 0 and e14.get().isdigit():
        mycursor.execute("ALTER TABLE grocery_list AUTO_INCREMENT=1")
        mycursor.execute("INSERT INTO grocery_list(product,brand,quantity,unit,price) VALUES(%s,%s,%s,%s,%s)",(e10.get(),e11.get(),e12.get(),e13.get(),e14.get()))
        mydb.commit()
    else:
        messagebox.showerror("Kitdy","Please check the data entered is correct or not")

def delete2():
    cursor = table1.focus()
    content = table1.item(cursor)
    row = content['values']
    temp = row[0]
    mycursor.execute("DELETE FROM grocery_list WHERE serial ="+str(temp))
    mydb.commit()

def show2():
    for i in table1.get_children():
        table1.delete(i)
    mycursor.execute("SELECT * FROM grocery_list")
    for i in mycursor.fetchall():
        table1.insert('' , 'end', values=i)

def search2():
    for i in table1.get_children():
        table1.delete(i)
    mycursor.execute("SELECT * FROM grocery_list WHERE product LIKE '%"+ e15.get() +"%'")
    for i in mycursor.fetchall():
        table1.insert('','end',value=i)

def buy2():
    import webbrowser
    cursor = table1.focus()
    content = table1.item(cursor)
    row = content['values']
    webbrowser.open('https://www.google.com/?#q='+row[1]+' '+row[2]+' '+str(row[3])+row[4]+' '+str(row[5])+' rupees')

def recipe():
    import webbrowser
    cursor = table.focus()
    content = table.item(cursor)
    row = content['values']
    webbrowser.open('https://www.allrecipes.com/search/results/?wt='+row[1])

root = Tk()
root.geometry("961x560")
root.maxsize(961,560)
root.minsize(961,560)
root.iconbitmap("C:/Users/acer pc/Desktop/My/Kitdy/kitdy.png")
root.title("Kitdy")

menu = Menu(root)
menu.add_command(label="Groceries",command=grocery)
menu.add_command(label="Buy",command=buy)
root.config(menu=menu)
d = date.today()
mycursor.execute("SELECT product,notify FROM groceries")
for i in mycursor.fetchall():
    if d == i[1]:
        temp = i[0]
        notification.notify(
            title="Product About to get Expire",
            message=temp,
            app_icon="C:/Users/acer pc/Desktop/kitdy.ico")

frame1 = Label(root)
frame2 = Frame(root)

se1=StringVar()
se2=StringVar()

Label(frame1,text="Kitdy",font=("times new roman", 24, "bold"),anchor="n",bg="red",relief=SUNKEN,bd=10).pack(fill=X)
side = Frame(frame1,bg="#CCCCCC",bd=5,height=800,width=400,relief=RIDGE)
side.place(x=0,y=58,height=300)
Label(side,text="Serial").grid(row=0,column=0)
Label(side,text="Product Name").grid(row=1,column=0,pady=12)
Label(side,text="Brand").grid(row=2,column=0)
Label(side,text="Quantity").grid(row=3,column=0,pady=12)
Label(side,text="Unit").grid(row=4,column=0)
Label(side,text="Expiry Date").grid(row=5,column=0,pady=12)
Label(side,text="Notify on").grid(row=6,column=0)
Label(side,text="Price").grid(row=7,column=0,pady=12)
Label(side,text="Purchased on").grid(row=8,column=0)

var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()
var6=StringVar()
var7=StringVar()
var8=StringVar()

e0=Entry(side,textvariable=se1,width=23,state='readonly')
e0.grid(row=0,column=1)
e1=Entry(side,textvariable=var1,width=23)
e1.grid(row=1,column=1)
e2=Entry(side,textvariable=var2,width=23)
e2.grid(row=2,column=1)
e3=Entry(side,textvariable=var3,width=23)
e3.grid(row=3,column=1)
e4=ttk.Combobox(side,textvariable=var4,state='readonly')
e4["values"]=("Kg","gm","L","ml")
e4.current(0)
e4.grid(row=4,column=1)
e5=Entry(side,textvariable=var5,width=23)
e5.grid(row=5,column=1)
e6=Entry(side,textvariable=var6,width=23,state='readonly')
e6.grid(row=6,column=1)
e7=Entry(side,textvariable=var7,width=23)
e7.grid(row=7,column=1)
e8=Entry(side,textvariable=var8,width=23)
e8.grid(row=8,column=1)
sidebutton = Frame(frame1,bd=5,bg="#CCCCCC",relief=RIDGE)
sidebutton.place(x=0,y=522,width=236)

b1 = Button(sidebutton,text="Add",command=insert).grid(row=7,column=0)
b2 = Button(sidebutton,text="Update",command=update).grid(row=7,column=1,padx=15)
b3 = Button(sidebutton,text="Delete",command=delete).grid(row=7,column=2)
b4 = Button(sidebutton,text="Clear",command=clear).grid(row=7,column=3,padx=15)

detail=Frame(frame1,bg="red")
detail.place(x=236,y=58,height=500,width=725)
tframe=Frame(detail,bg="yellow")
tframe.place(x=28,y=40,width=670)
scrx=Scrollbar(tframe,orient=HORIZONTAL)
scrx.pack(side=BOTTOM,fill=X)
scry=Scrollbar(tframe,orient=VERTICAL)
scry.pack(side=RIGHT,fill=Y)
table=ttk.Treeview(tframe,columns=("S.No","Product","Brand","Quantity","Unit","Expire","Notify","Price","Purchased On"),xscrollcommand=scrx.set,yscrollcommand=scry.set)
scrx.config(command=table.xview) 
scry.config(command=table.yview)

table.heading("S.No",text="S.No")
table.heading("Product",text="Product")
table.heading("Brand",text="Brand")
table.heading("Quantity",text="Quantity")
table.heading("Unit",text="Unit")
table.heading("Expire",text="Expire")
table.heading("Notify",text="Notify")
table.heading("Price",text="Price")
table.heading("Purchased On",text="Purchased On")
table['show']='headings'

table.column("S.No",width=60,minwidth=60)
table.column("Product",width=100,minwidth=100)
table.column("Brand",width=100,minwidth=100)
table.column("Quantity",width=60,minwidth=60)
table.column("Unit",width=40,minwidth=40)
table.column("Expire",width=80,minwidth=80)
table.column("Notify",width=80,minwidth=80)
table.column("Price",width=50,minwidth=50)
table.column("Purchased On",width=80,minwidth=80)
table.pack()
table.bind("<ButtonRelease-1>",cursor)

Label(detail,text="Search By Product",bg="yellow").place(x=28,y=320)
Label(detail,text="Graph",bg="yellow").place(x=28,y=360)
e9=Entry(detail)
e9.place(x=150,y=320)
e17=Entry(detail)
e17.place(x=78,y=360)
b5=Button(detail,text="Search",command=search).place(x=290,y=320)
b6=Button(detail,text="Show All",command=show).place(x=350,y=320)
b14=Button(detail,text="Recipe",command=recipe).place(x=420,y=320)
b15=Button(detail,text="Ok",command=graph).place(x=220,y=360)
#################################  BUY ###############################

Label(frame2,text="Kitdy",font=("times new roman", 24, "bold"),anchor="n",bg="red",relief=SUNKEN,bd=10).pack(fill=X)
side = Frame(frame2,bg="#CCCCCC",bd=5,height=800,width=400,relief=RIDGE)
side.place(x=0,y=58,height=240)
Label(side,text="Serial").grid(row=0,column=0)
Label(side,text="Product Name").grid(row=1,column=0,pady=20)
Label(side,text="Brand").grid(row=2,column=0)
Label(side,text="Quantity").grid(row=3,column=0,pady=20)
Label(side,text="Unit").grid(row=4,column=0)
Label(side,text="Price").grid(row=5,column=0,pady=20)

var9=StringVar()
var10=StringVar()
var11=StringVar()
var12=StringVar()
var13=StringVar()

e16=Entry(side,textvariable=se2,width=23,state='readonly')
e16.grid(row=0,column=1)
e10=Entry(side,textvariable=var9,width=23)
e10.grid(row=1,column=1)
e11=Entry(side,textvariable=var10,width=23)
e11.grid(row=2,column=1)
e12=Entry(side,textvariable=var11,width=23)
e12.grid(row=3,column=1)
e13=ttk.Combobox(side,textvariable=var12,state='readonly')
e13["values"]=("Kg","gm","L","ml")
e13.current(0)
e13.grid(row=4,column=1)
e14=Entry(side,textvariable=var13,width=23)
e14.grid(row=5,column=1)
sidebutton = Frame(frame2,bd=5,bg="#CCCCCC",relief=RIDGE)
sidebutton.place(x=0,y=522,width=236)

b7 = Button(sidebutton,text="Add",command=insert2).grid(row=7,column=0)
b8 = Button(sidebutton,text="Update",command=update2).grid(row=7,column=1,padx=15)
b9 = Button(sidebutton,text="Delete",command=delete2).grid(row=7,column=2)
b10 = Button(sidebutton,text="Clear",command=clear2).grid(row=7,column=3,padx=15)

detail1=Frame(frame2,bg="red")
detail1.place(x=236,y=58,height=500,width=725)
tframe1=Frame(detail1,bg="yellow")
tframe1.place(x=28,y=40,width=670)
scrx=Scrollbar(tframe1,orient=HORIZONTAL)
scrx.pack(side=BOTTOM,fill=X)
scry=Scrollbar(tframe1,orient=VERTICAL)
scry.pack(side=RIGHT,fill=Y)
table1=ttk.Treeview(tframe1,columns=("S.No","Product","Brand","Quantity","Unit","Price"),xscrollcommand=scrx.set,yscrollcommand=scry.set)
scrx.config(command=table1.xview) 
scry.config(command=table1.yview)

table1.heading("S.No",text="S.No")
table1.heading("Product",text="Product")
table1.heading("Brand",text="Brand")
table1.heading("Quantity",text="Quantity")
table1.heading("Unit",text="Unit")
table1.heading("Price",text="Price")
table1['show']='headings'

table1.column("S.No",width=60,minwidth=60)
table1.column("Product",width=200,minwidth=100)
table1.column("Brand",width=200,minwidth=100)
table1.column("Quantity",width=80,minwidth=60)
table1.column("Unit",width=50,minwidth=40)
table1.column("Price",width=60,minwidth=50)
table1.pack()
table1.bind("<ButtonRelease-1>",cursor2)

Label(detail1,text="Search By Product",bg="yellow").place(x=28,y=320)
e15=Entry(detail1)
e15.place(x=150,y=320)
b11=Button(detail1,text="Search",command=search2).place(x=290,y=320)
b12=Button(detail1,text="Show All",command=show2).place(x=350,y=320)
b13=Button(detail1,text="Buy",command=buy2).place(x=420,y=320)

root.mainloop()
mycursor.close()
mydb.close()