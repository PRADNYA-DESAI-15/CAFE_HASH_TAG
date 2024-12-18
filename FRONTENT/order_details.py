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
    C_id=box1.get()
    o_place=box2.get()
    order=box3.get()
    Pay=box4.get()

    cur = conn.cursor()
    sql = "insert into order_details(customer_ID,place,Order1,total_payment) values ('" + C_id + "','" + o_place + "','" + order + "','" + Pay + "' );"
    result = cur.execute(sql)
    messagebox.showinfo("Success", "Data inserted successfully")
    conn.commit()
    cur.close()

def Exit():
    os.system("menu.py")


root=Tk()
root.geometry("1366x768+0+0")
root.configure(bg="sky blue")
root.title("CAFE #_TAG")

image_1=Image.open( "D:\pictures\Saved Pictures\Coffee_Cup_Grain_513119_1366x768.jpg")
bck_end=ImageTk.PhotoImage(image_1)
mainlabel=Label(root,image=bck_end)
mainlabel.place(x=0,y=0)


myframe = Frame(root, bg="black", height=500, width=700)
myframe.place(x=350, y=70)

frame2 = Frame(myframe, bg="yellow", height=100, width=700)
frame2.place(x=0, y=0)

mainlabel=Label(root,text="ORDER DETAILS",bg="yellow",font=("Action Man Shaded",30,"bold"))
mainlabel.place(x=540,y=85)

mainlabel1=Label(root,text="Customer ID:",fg="white",bg="black",font=("Action Man",15))
mainlabel1.place(x=430,y=230)
box1=Entry(root,font=("Action Man",15))
box1.place(x=430,y=270)

mainlabel2=Label(root,text="Order Place :",fg="white",bg="black",font=("Action Man",15))
mainlabel2.place(x=730,y=230)
box2=Entry(root,font=("Action Man",15))
box2.place(x=730,y=270)

mainlabel3=Label(root,text="Order :",fg="white",bg="black",font=("Action Man",15))
mainlabel3.place(x=430,y=330)
box3=Entry(root,font=("Action Man",15))
box3.place(x=430,y=370)

mainlabel4=Label(root,text="Total Payment :",fg="white",bg="black",font=("Action Man",15))
mainlabel4.place(x=730,y=330)
box4=Entry(root,font=("Action Man",15))
box4.place(x=730,y=370)

B1=Button(root,text="  SAVE  ",fg="white",bg="black",command=save ,font=("Action Man",16))
B1.place(x=520,y=460)

B2=Button(root,text="  BACK  ",fg="white",bg="black",font=("Action Man",16),command=Exit)
B2.place(x=750,y=460)


root.mainloop()