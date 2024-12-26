from tkinter import *
import mysql.connector
from tkinter import ttk
from PIL import ImageTk, Image

# Connect to the database
conn = mysql.connector.connect(host="localhost", user="root", password="pradnya1512", database="cafe_hash_tag")
if conn.is_connected():
    print("Connection successful")
else:
    print("Connection failed")

# Exit function
def Exit():
    root.destroy()

# Function to add selected item to the bill
def add_to_order(event):
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item, "values")
        menu_name, category, price = item
        order_tree.insert("", END, values=(menu_name, category, price))
        update_total(price)

# Function to update the total bill
def update_total(price):
    global total
    total += float(price)
    total_label.config(text=f"Total: ₹{total:.2f}")

# Function to save the order to the database
def save_order():
    global total
    order_ID = box1.get()
    customer_ID = box2.get()

    if not customer_ID:
        error_label.config(text="Customer ID is required!", fg="red")
        return

    cur = conn.cursor()
    total = 0  # Reset total for each order

    # Calculate total from the order tree
    for row in order_tree.get_children():
        values = order_tree.item(row, "values")
        price = values[2]  # Assuming price is the third column
        total += float(price)

    # Insert or update the order in the database
    sql = "INSERT INTO orders (Order_ID, price, Customer_ID) VALUES (%s, %s, %s)"
    sql_update = "UPDATE orders SET price = %s WHERE Order_ID = %s"

    try:
        cur.execute(sql, (order_ID, total, customer_ID))
        print("Order inserted")
    except mysql.connector.IntegrityError as e:
        if '1062' in str(e):  # Duplicate Order_ID
            cur.execute(sql_update, (total, order_ID))
            print("Order updated")

    # Save order details to final_order
    sql1 = """
        INSERT INTO final_order (Order_ID, Price, Customer_ID, Customer_Name, Customer_Surname)
        SELECT 
            o.Order_ID, 
            o.Price, 
            c.Customer_ID, 
            c.firstname, 
            c.lastname
        FROM 
            Orders o
        JOIN 
            customer_details c
        ON 
            o.Customer_ID = c.Customer_ID
        GROUP BY 
            o.Order_ID, o.Price, c.Customer_ID, c.firstname, c.lastname;
    """
    try:
        cur.execute(sql1)
        print("Order details added to final_order")
    except mysql.connector.Error as e:
        print(f"Error inserting into Final_Order: {e}")
    conn.commit()
    error_label.config(text="Order saved successfully!", fg="green")
    order_tree.delete(*order_tree.get_children())
   # global total

    total_label.config(text=f"Total: ₹{total:.2f}")


def fetch_next_Order_id():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT COALESCE(MAX(Order_ID), 0) + 1 FROM orders")
        return cursor.fetchone()[0]
    except Exception as e:
        print(f"Error: {e}")
        return "Error"


# Initialize the main window
root = Tk()
root.geometry("1366x768+0+0")
root.configure(bg="sky blue")
root.title("CAFE #_TAG")

total = 0.0  # Initialize total amount

# Background image
image_1 = Image.open("D:\\pictures\\Saved Pictures\\Coffee_Cup_Grain_513119_1366x768.jpg")
bck_end = ImageTk.PhotoImage(image_1)
mainlabel = Label(root, image=bck_end)
mainlabel.place(x=0, y=0)

# Header frame
frame2 = Frame(root, bg="yellow", height=100, width=1366)
frame2.place(x=0, y=0)

# Menu Treeview
columns = ('C1', 'C2', 'C3')
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.column("#1", width=150)
tree.heading("#1", text="Menu Name")
tree.column("#2", width=150)
tree.heading("#2", text="Category")
tree.column("#3", width=150)
tree.heading("#3", text="Menu Price")
tree.place(x=100, y=170)

tree.bind("<Double-1>", add_to_order)  # Bind double-click to add_to_order function

# Menu Card Label
mainlabel = Label(root, text="MENU CARD", bg="yellow", font=("Action Man Shaded", 30, "bold"))
mainlabel.place(x=550, y=25)

# Customer ID
mainlabel = Label(root, text="Order_ID:", bg="black", fg="white", font=("Action Man", 15))
mainlabel.place(x=750, y=120)

box1 = Entry(root, font=("Action Man", 15))
box1.place(x=880, y=120)
box1.configure(state="normal")
box1.insert(0, fetch_next_Order_id())
box1.configure(state="readonly")

mainlabel = Label(root, text="Customer_ID:", bg="black" ,fg="white" , font=("Action Man",15))
mainlabel.place(x=350, y=120)

box2=Entry(root, font=("Action Man",15))
box2.place(x=500 ,y=120)

# Buttons
B1 = Button(root, text="SAVE ORDER", fg="white", bg="black", command=save_order, font=("Action Man", 12, "underline"))
B1.place(x=1100, y=120)

B2 = Button(root, text="EXIT", fg="white", bg="black", command=Exit, font=("Action Man", 12, "underline"))
B2.place(x=1250, y=120)

# Error/Success Label
error_label = Label(root, text="", bg="sky blue", font=("Action Man", 12, "bold"))
error_label.place(x=750, y=160)

# Order Treeview
order_tree = ttk.Treeview(root, columns=columns, show="headings")
order_tree.column("#1", width=150)
order_tree.heading("#1", text="Menu Name")
order_tree.column("#2", width=150)
order_tree.heading("#2", text="Category")
order_tree.column("#3", width=150)
order_tree.heading("#3", text="Menu Price")
order_tree.place(x=800, y=250)

# Total Label
total_label = Label(root, text=f"Total: ₹0.00", bg="yellow", font=("Action Man", 15, "bold"))
total_label.place(x=1100, y=500)

# Populate Menu Treeview
cur = conn.cursor(buffered=True)
sql = "SELECT * FROM menu_details"
cur.execute(sql)
rows = cur.fetchall()
for row in rows:
    tree.insert("", END, values=row)

# Run the application
root.mainloop()