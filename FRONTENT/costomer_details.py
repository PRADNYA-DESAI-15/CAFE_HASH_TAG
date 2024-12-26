from tkinter import *
import mysql.connector
from  tkinter import messagebox
from tkinter import ttk
import os
from PIL import ImageTk, Image
import  datetime

conn=mysql.connector.connect(host="localhost",user="root",password="pradnya1512",database="cafe_hash_tag")
if(conn.is_connected()):
    print("connection succesfully")
else:
    print("connection failed")





def save():
    C_id=box1.get()
    fname=box2.get()
    lname=box3.get()
    add=box4.get()
    contact=box5.get()
    gender=var.get()
    id_p=var1.get()
    id_n= box8.get()
    time_1=box10.get()
    date_1=box9.get()
    print(fname)

    cur = conn.cursor()
    sql = "insert into customer_details(customer_ID,firstname,lastname,Contact,Address,ID_proof,ID_No,gender,date1,time1) values ('" + C_id + "','" + fname + "','" + lname + "','" + add + "','" + contact + "','" + gender + "','" + id_p + "','" + id_n + "','"+ date_1 +"' ,'"+ time_1 +"' );"
    result=cur.execute(sql)
    messagebox.showinfo("Success", "Data inserted successfully")
    conn.commit()
    cur.close()

def Exit():
    os.system("home.py")


def fetch_next_customer_id():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT COALESCE(MAX(Customer_ID), 0) + 1 FROM customer_details")
        return cursor.fetchone()[0]
    except Exception as e:
        print(f"Error: {e}")
        return "Error"

root=Tk()
root.geometry("1366x768+0+0")
root.configure(bg="sky blue")
root.title("CAFE #_TAG")

image_1=Image.open( "D:\pictures\Saved Pictures\Coffee_Cup_Grain_513119_1366x768.jpg")
bck_end=ImageTk.PhotoImage(image_1)
mainlabel=Label(root,image=bck_end)
mainlabel.place(x=0,y=0)

myframe = Frame(root, bg="black", height=600, width=800)
myframe.place(x=300, y=70)

frame2 = Frame(myframe, bg="yellow", height=100, width=800)
frame2.place(x=0, y=0)

mainlabela=Label(root,text="CUSTOMER DETAILS",bg="yellow",font=("Action Man Shaded",30,"bold"))
mainlabela.place(x=500,y=85)

mainlabel1=Label(root,text="Customer_ID:", fg="white",bg="black",font=("Action Man",15,"bold" ))
mainlabel1.place(x=400,y=200)
box1=ttk.Entry(root,font=("Action Man",15))
box1.place(x=400,y=230)
box1.configure(state="normal")
box1.insert(0, fetch_next_customer_id())
box1.configure(state="readonly")


mainlabel2=Label(root,text="First Name :", fg="white",bg="black",font=("Action Man",15))
mainlabel2.place(x=400,y=280)
box2=Entry(root,font=("Action Man",15))
box2.place(x=400,y=310)

mainlabel3=Label(root,text="Last Name :",fg="white",bg="black",font=("Action Man",15))
mainlabel3.place(x=400,y=360)
box3=Entry(root,font=("Action Man",15))
box3.place(x=400,y=390)


mainlabel4=Label(root,text="Contact :",fg="white",bg="black",font=("Action Man",15))
mainlabel4.place(x=400,y=440)
box4=Entry(root,font=("Action Man",15))
box4.place(x=400,y=470)

mainlabel5=Label(root,text="Address :",fg="white",bg="black",font=("Action Man",15))
mainlabel5.place(x=750,y=440)
box5=Entry(root,font=("Action Man",15))
box5.place(x=750,y=470)

mainlabel6=Label(root,text="Gender :",fg="white",bg="black",font=("Action Man",15))
mainlabel6.place(x=750,y=360)
var=StringVar(root)
var.set("Gender")
box6=OptionMenu(root,var,'Male', 'Female', 'Other')
box6.place(x=750,y=390)


mainlabel7=Label(root,text="ID Proof :",fg="white",bg="black",font=("Action Man",15))
mainlabel7.place(x=750,y=200)
var1=StringVar(root)
var1.set("Card")
box7=OptionMenu(root,var1,'Voting Card', 'Pan Card', 'Aadhar Card')
box7.place(x=750,y=230)

mainlabel8=Label(root,text="ID No   :",fg="white",bg="black",font=("Action Man",15))
mainlabel8.place(x=750,y=280)
box8=Entry(root,font=("Action Man",15))
box8.place(x=750,y=310)

date = datetime.datetime.now()
mainlabel9=Label(root,text="Date :",fg="white",bg="black",font=("Action Man",15))
mainlabel9.place(x=400,y=520)
box9=Entry(root,font=("Action Man",15))
box9.insert(END, f"{date:%b %d, %Y}")
box9.place(x=400,y=550)


time = datetime.datetime.now().time()
mainlabel10=Label(root,text="Time :",fg="white",bg="black",font=("Action Man",15))
mainlabel10.place(x=750,y=520)
box10=Entry(root,font=("Action Man",15))
box10.insert(END, time)
box10.place(x=750,y=550)


B1=Button(root,text="  SAVE  ",fg="white",bg="black",command=save,font=("Action Man",16,"bold"))
B1.place(x=520,y=600)

B1=Button(root,text="  CANCEL  ",fg="white",bg="black",font=("Action Man",16,"bold"),command=Exit)
B1.place(x=750,y=600)



root.mainloop()

