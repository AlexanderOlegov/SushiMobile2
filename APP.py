import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

root = Tk()
root.geometry("900x900")
def Prices():    
    roy = Tk()    
    roy.geometry("900x900")
    tk.Label(roy, text="Сведения о стоимости доставки", fg="red", font=(None, 30)).place(x=300, y=5)
    tk.Label(roy, text="ID").place(x=10, y=10)
    Label(roy, text="Стоимость").place(x=10, y=40)
    Label(roy, text="ТипДоставки").place(x=10, y=70)
    Label(roy, text="Компания").place(x=10, y=100)
    e1 = Entry(roy)
    e1.place(x=140, y=10)
    e2 = Entry(roy)
    e2.place(x=140, y=40)
    e3 = Entry(roy)
    e3.place(x=140, y=70)
    e4 = Entry(roy)
    e4.place(x=140, y=100)
       
    def Insert():
        studid = e1.get()
        studname = e2.get()
        coursename = e3.get()
        feee = e4.get()
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="sushimarket")
        mycursor=mysqldb.cursor()
        try:
           sql = "INSERT INTO  delivery (id,Cost,Type,Company) VALUES (%s, %s, %s, %s)"
           val = (studid,studname,coursename,feee)
           mycursor.execute(sql, val)
           mysqldb.commit()
           lastid = mycursor.lastrowid
           messagebox.showinfo("information", "Добавлены сведения о доставке")
           e1.delete(0, END)
           e2.delete(0, END)
           e3.delete(0, END)
           e4.delete(0, END)
           e1.focus_set()
        except Exception as e:
           print(e)
           mysqldb.rollback()
           mysqldb.close()
    def update():
        studid = e1.get()
        studname = e2.get()
        coursename = e3.get()
        feee = e4.get()
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="sushimarket")
        mycursor=mysqldb.cursor()
        sql = "Update  delivery set Cost= %s,Type= %s,Company= %s where id= %s"
        val = (studid,coursename,feee,studid)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("Информация", "Данные изменены")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    def delete():
        studid = e1.get()        
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="sushimarket")
        mycursor=mysqldb.cursor()
        sql = "delete from delivery where id= %s"
        val = (studid,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("Информация", "Данные удалены")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    def GetValue(event):
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        row_id = listbox.selection()[0]
        select = listbox.set(row_id)
        e1.insert(0,select['id'])
        e2.insert(0,select['Cost'])
        e3.insert(0,select['Type'])
        e4.insert(0,select['Company'])
    def show():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="sushimarket")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT id,Cost,Type,Company FROM delivery")
        records = mycursor.fetchall()
        print(records)
        for i, (studid,studname, coursename,feee) in enumerate(records, start=1):
            listbox.insert("", "end", values=(studid, studname, coursename, feee))
            mysqldb.close()

    cols = ('id','Цена','Вид','Статус')
    listbox = ttk.Treeview(roy,columns=cols,show='headings')
    for col in cols:
        listbox.heading(col, text=col)
        listbox.grid(row=1, column=0, columnspan=2)
        listbox.place(x=10, y=200)
    listbox.bind('<Double-Button-1>', GetValue)
    show()
    Button(roy, text="Добавить",height=3, width= 13,command=Insert).place(x=30, y=130)
    Button(roy, text="Обновить",height=3, width= 13,command=update).place(x=30, y=430)
    Button(roy, text="Удалить",height=3, width= 13,command=delete).place(x=140, y=430)

    cols = ('id', 'empname', 'mobile','salary')
def Delivers():
    roy2 = Tk()    
    roy2.geometry("900x900")
    tk.Label(roy2, text="Сведения о курьерах Суши-Маркет", fg="red", font=(None, 30)).place(x=300, y=5)
    tk.Label(roy2, text="ID").place(x=10, y=10)
    Label(roy2, text="ФИО").place(x=10, y=40)
    Label(roy2, text="ДатаРождения").place(x=10, y=70)
    Label(roy2, text="Статус").place(x=10, y=100)
    Label(roy2, text="ВидДеятельности").place(x=10, y=100)
    d1 = Entry(roy2)
    d1.place(x=140, y=10)
    d2 = Entry(roy2)
    d2.place(x=140, y=40)
    d3 = Entry(roy2)
    d3.place(x=140, y=70)
    d4 = Entry(roy2)
    d4.place(x=140, y=100)
    d5 = Entry(roy2)
    d5.place(x=140, y=100)
    def Insert2():
        studid = d1.get()
        studname = d2.get()
        coursename = d3.get()
        feee = d4.get()
        feee2 = d5.get()
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="sushimarket")
        mycursor=mysqldb.cursor()
        try:
           sql = "INSERT INTO  delivers (id,FIO,DateOfBirth,Status,Job) VALUES (%s, %s, %s, %s, %s)"
           val2 = (studid,studname,coursename,feee,feee2)
           mycursor.execute(sql, val2)
           mysqldb.commit()
           lastid = mycursor.lastrowid
           messagebox.showinfo("information", "Добавлены сведения о курьере")
           d1.delete(0, END)
           d2.delete(0, END)
           d3.delete(0, END)
           d4.delete(0, END)
           d5.focus_set()
        except Exception as e:
           print(e)
           mysqldb.rollback()
           mysqldb.close()
    def update2():
        studid = d1.get()
        studname = d2.get()
        coursename = d3.get()
        feee = d4.get()
        feee2 = d5.get()
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="sushimarket")
        mycursor=mysqldb.cursor()
        sql = "Update  delivers set FIO= %s,DateOfBirth= %s,Status= %s,Job= %s where id= %s"
        val = (studid,coursename,feee,feee2,studid)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("Информация", "Данные о доставщике изменены")
        d1.delete(0, END)
        d2.delete(0, END)
        d3.delete(0, END)
        d4.delete(0, END)
        d5.delete(0, END)
        d1.focus_set()
    def delete2():
        studid = d1.get()        
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="sushimarket")
        mycursor=mysqldb.cursor()
        sql = "delete from delivers where id= %s"
        val = (studid,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("Информация", "Данные удалены")
        d1.delete(0, END)
        d2.delete(0, END)
        d3.delete(0, END)
        d4.delete(0, END)
        d5.delete(0, END)
        d1.focus_set()
    def GetValue(event):
        d1.delete(0, END)
        d2.delete(0, END)
        d3.delete(0, END)
        d4.delete(0, END)
        d5.delete(0, END)
        row_id = listbox.selection()[0]
        select = listbox.set(row_id)
        d1.insert(0,select['id'])
        d2.insert(0,select['FIO'])
        d3.insert(0,select['DateOfBirth'])
        d4.insert(0,select['Status'])
        d5.insert(0,select['Job'])
    def show():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="sushimarket")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT id,FIO,DateOfBirth,Status,Job FROM delivers")
        records = mycursor.fetchall()
        print(records)
        for i, (studid,studname, coursename,feee,feee2) in enumerate(records, start=1):
            listbox.insert("", "end", values=(studid, studname, coursename, feee, feee2))
            mysqldb.close()

    cols = ('id','ФИО','ДатаРождения','Статус','Вид деятельности')
    listbox = ttk.Treeview(roy2,columns=cols,show='headings')
    for col in cols:
        listbox.heading(col, text=col)
        listbox.grid(row=1, column=0, columnspan=2)
        listbox.place(x=10, y=200)
    listbox.bind('<Double-Button-1>', GetValue)
    show()

    Button(roy2, text="Добавить",height=3, width= 13,command=Insert2).place(x=30, y=130)
    Button(roy2, text="Обновить",height=3, width= 13,command=update2).place(x=230, y=430)
    Button(roy2, text="Удалить",height=3, width= 13,command=delete2).place(x=30, y=430)
  
    cols = ('id', 'empname', 'mobile','salary')
def Orders():
    roy3 = Tk()    
    roy3.geometry("900x900")
    tk.Label(roy3, text="Сведения о заказах Суши-Маркет", fg="red", font=(None, 30)).place(x=300, y=5)
    tk.Label(roy3, text="ID").place(x=10, y=10)
    Label(roy3, text="Наименование").place(x=10, y=40)
    Label(roy3, text="Стоимость заказа").place(x=10, y=70)
    Label(roy3, text="Статус").place(x=10, y=100)    
    h1 = Entry(roy3)
    h1.place(x=140, y=10)
    h2 = Entry(roy3)
    h2.place(x=140, y=40)
    h3 = Entry(roy3)
    h3.place(x=140, y=70)
    h4 = Entry(roy3)
    h4.place(x=140, y=100)    
    def Insert3():
        studid = h1.get()
        studname = h2.get()
        coursename = h3.get()
        feee = h4.get()        
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="sushimarket")
        mycursor=mysqldb.cursor()
        try:
           sql = "INSERT INTO  orders (id,Name,Cost,Status) VALUES (%s, %s, %s, %s)"
           val2 = (studid,studname,coursename,feee)
           mycursor.execute(sql, val2)
           mysqldb.commit()
           lastid = mycursor.lastrowid
           messagebox.showinfo("information", "Заказ оформлен")
           h1.delete(0, END)
           h2.delete(0, END)
           h3.delete(0, END)
           h4.focus_set()
        except Exception as e:
           print(e)
           mysqldb.rollback()
           mysqldb.close()    
    def update3():
        studid = h1.get()
        studname = h2.get()
        coursename = h3.get()
        feee = h4.get()        
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="sushimarket")
        mycursor=mysqldb.cursor()
        sql = "Update  orders set Name= %s,Cost= %s,Status= %s where id= %s"
        val = (studid,coursename,feee,studid)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("Информация", "Статус заказа изменен")
        h1.delete(0, END)
        h2.delete(0, END)
        h3.delete(0, END)
        h4.delete(0, END)
        h1.focus_set()
    def delete3():
        studid = h1.get()        
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="sushimarket")
        mycursor=mysqldb.cursor()
        sql = "delete from orders where id= %s"
        val = (studid,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("Информация", "Данные удалены")
        h1.delete(0, END)
        h2.delete(0, END)
        h3.delete(0, END)
        h4.delete(0, END)        
        h1.focus_set()
    def GetValue(event):
        h1.delete(0, END)
        h2.delete(0, END)
        h3.delete(0, END)
        h4.delete(0, END)
        row_id = listbox.selection()[0]
        select = listbox.set(row_id)
        h1.insert(0,select['id'])
        h2.insert(0,select['Name'])
        h3.insert(0,select['Cost'])
        h4.insert(0,select['Status'])
    def show():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="sushimarket")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT id,Name,Cost,Status FROM orders")
        records = mycursor.fetchall()
        print(records)
        for i, (studid,studname, coursename,feee) in enumerate(records, start=1):
            listbox.insert("", "end", values=(studid, studname, coursename, feee))
            mysqldb.close()

    cols = ('id','Наименование','Цена','Статус')
    listbox = ttk.Treeview(roy3,columns=cols,show='headings')
    for col in cols:
        listbox.heading(col, text=col)
        listbox.grid(row=1, column=0, columnspan=2)
        listbox.place(x=10, y=200)
    listbox.bind('<Double-Button-1>', GetValue)
    show()

    Button(roy3, text="Добавить",height=3, width= 13,command=Insert3).place(x=30, y=130)
    Button(roy3, text="Обновить",height=3, width= 13,command=update3).place(x=30, y=430)
    Button(roy3, text="Удалить",height=3, width= 13,command=delete3).place(x=130, y=430)
Buy = Button(root,text="Сведения о стоимости доставки", bd=0,background="Aqua",font="Impact",command=Prices)
Buy.place(x=390,y=20)
Buy2 = Button(root,text="Сведения о курьерах",command=Delivers, bd=0,background="Aqua",font="Impact")
Buy2.place(x=390,y=90)

Buy4 = Button(root,text="Сведения о заказах Суши маркет", command=Orders,bd=0,background="Aqua",font="Impact")
Buy4.place(x=390,y=180)
root.mainloop()

