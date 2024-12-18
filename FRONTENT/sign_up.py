from tkinter import *
import mysql.connector
from  tkinter import messagebox
from PIL import ImageTk, Image
import os

conn=mysql.connector.connect(host="localhost",user="root",password="pradnya1512",database="cafe_hash_tag")
if(conn.is_connected()):
    print("connection succesfully")
else:
    print("connection failed")

def save():
    CN=box1.get()
    cont=box3.get()
    gmail=box2.get()
    password=box4.get()
    print(CN)

    cur = conn.cursor()
    sql = "insert into sign_up(customer_name,contact,gmail,pass) values ('" + CN + "','" + cont + "','" + gmail + "','" + password + "' );"
    result = cur.execute(sql)
    messagebox.showinfo("Success", "Data inserted successfully")
    conn.commit()
    cur.close()


def cancel():
    os.system("login.py")


root=Tk()
root.geometry("1366x768+0+0")

image_1=Image.open( "D:\pictures\Saved Pictures\Coffee_Cup_Grain_513119_1366x768.jpg")
bck_end=ImageTk.PhotoImage(image_1)
mainlabel=Label(root,image=bck_end)
mainlabel.place(x=0,y=0)

root.title("CAFE #_TAG")

myframe = Frame(root, bg="black", height=500, width=700)
myframe.place(x=350, y=70)

frame2 = Frame(myframe, bg="yellow", height=100, width=700)
frame2.place(x=0, y=0)

mainlabel=Label(root,text="SIGN UP",bg="yellow",font=("Action Man Shaded",30,"bold"))
mainlabel.place(x=620,y=85)

mainlabel1=Label(root,text="Customer Name:",fg="white",bg="black",font=("Action Man",15))
mainlabel1.place(x=430,y=230)
box1=Entry(root,font=("Action Man",15))
box1.place(x=430,y=270)

mainlabel2=Label(root,text="Gmail :",fg="white",bg="black",font=("Action Man",15))
mainlabel2.place(x=730,y=230)
box2=Entry(root,font=("Action Man",15))
box2.place(x=730,y=270)

mainlabel3=Label(root,text="Contact :",fg="white",bg="black",font=("Action Man",15))
mainlabel3.place(x=430,y=330)
box3=Entry(root,font=("Action Man",15))
box3.place(x=430,y=370)

mainlabel4=Label(root,text="Password :",fg="white",bg="black",font=("Action Man",15))
mainlabel4.place(x=730,y=330)
box4=Entry(root,font=("Action Man",15))
box4.place(x=730,y=370)

B1=Button(root,text="  SAVE  ",fg="white",bg="black",command=save,font=("Action Man",16))
B1.place(x=520,y=460)

B2=Button(root,text="  CANCEL  ",fg="white",bg="black",font=("Action Man",16),command=cancel)
B2.place(x=750,y=460)

root.mainloop()