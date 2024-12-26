import os
from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk, Image

conn = mysql.connector.connect(host="localhost", user="root", password="pradnya1512", database="cafe_hash_tag")
if conn.is_connected():
    print("Connection successful")
else:
    print("Connection failed")

def save():
    C_ID = box1.get()
    Payment = box3.get()
    CN = box2.get()
    Mode = box4.get()
    print(CN)

    cur = conn.cursor()
    sql = "INSERT INTO payment_details(customer_ID, customer_name, total_payment, payment_method) VALUES (%s, %s, %s, %s)"
    cur.execute(sql, (C_ID, CN, Payment, Mode))
    messagebox.showinfo("Success", "Data inserted successfully")
    conn.commit()
    cur.close()

def Exit():
    os.system("login.py")


def fetch_customer_details():
    customer_id = box1.get()
    if not customer_id:
        messagebox.showerror("Error", "Customer ID is required!")
        return

    try:
        cur = conn.cursor()
        sql = "SELECT Customer_Name, Price FROM final_order WHERE Customer_ID = %s"
        cur.execute(sql, (customer_id,))
        result = cur.fetchone()
        if result:
            customer_name, price = result
            box2.delete(0, END)
            box2.insert(0, customer_name)
            box3.delete(0, END)
            box3.insert(0, price)
            messagebox.showinfo("Success", "Customer details fetched successfully")
        else:
            messagebox.showwarning("Warning", "No details found for the given Customer ID")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch customer details: {e}")
    finally:
        cur.close()

root = Tk()
root.geometry("1366x768+0+0")
root.configure(bg="sky blue")
root.title("CAFE #_TAG")

image_1 = Image.open("D:\\pictures\\Saved Pictures\\Coffee_Cup_Grain_513119_1366x768.jpg")
bck_end = ImageTk.PhotoImage(image_1)
mainlabel = Label(root, image=bck_end)

mainlabel.place(x=0, y=0)

myframe = Frame(root, bg="black", height=500, width=700)
myframe.place(x=350, y=70)

frame2 = Frame(myframe, bg="yellow", height=100, width=700)
frame2.place(x=0, y=0)

mainlabel = Label(root, text="PAYMENT DETAILS", bg="yellow", font=("action man shaded", 25, "bold"))
mainlabel.place(x=550, y=100)

mainlabel1 = Label(root, text="Customer ID:", fg="white", bg="black", font=("Action Man", 15))
mainlabel1.place(x=430, y=230)
box1 = Entry(root, font=("Action Man", 15))
box1.place(x=430, y=270)

mainlabel2 = Label(root, text="Customer Name:", fg="white", bg="black", font=("Action Man", 15))
mainlabel2.place(x=730, y=230)
box2 = Entry(root, font=("Action Man", 15))
box2.place(x=730, y=270)

mainlabel3 = Label(root, text="Total Payment:", fg="white", bg="black", font=("Action Man", 15))
mainlabel3.place(x=430, y=330)
box3 = Entry(root, font=("Action Man", 15))
box3.place(x=430, y=370)

mainlabel4 = Label(root, text="Payment Method:", fg="white", bg="black", font=("Action Man", 15))
mainlabel4.place(x=730, y=330)
box4 = Entry(root, font=("Action Man", 15))
box4.place(x=730, y=370)

# Add buttons
B1 = Button(root, text="  SAVE  ", fg="white", bg="black", font=("Action Man", 16, "bold"), command=save)
B1.place(x=800, y=460)

B2 = Button(root, text="  CANCEL  ", fg="white", bg="black", font=("Action Man", 16, "bold"), command=Exit)
B2.place(x=460, y=460 )

B3 = Button(root, text="FETCH DETAILS", fg="white", bg="black", font=("Action Man", 16, "bold"), command=fetch_customer_details)
B3.place(x=610, y=460)

root.mainloop()
