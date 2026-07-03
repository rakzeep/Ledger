import tkinter as tk
from tkinter import messagebox, simpledialog
import mysql.connector
import numpy as np

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="bankdb"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS account (
    id INT PRIMARY KEY,
    balance DOUBLE
)
""")

cursor.execute("SELECT * FROM account WHERE id = 1")
result = cursor.fetchone()

if result is None:
    cursor.execute("INSERT INTO account VALUES (1, 0)")
    conn.commit()

def get_balance():
    cursor.execute("SELECT balance FROM account WHERE id = 1")
    balance = cursor.fetchone()[0]
    return np.array([balance])

def update_balance(balance):
    cursor.execute(
        "UPDATE account SET balance = %s WHERE id = 1",
        (float(balance[0]),)
    )
    conn.commit()

def show_balance():
    balance = get_balance()
    messagebox.showinfo("Balance", f"Your balance is ${balance[0]:.2f}")

def deposit():
    amount = simpledialog.askfloat("Deposit", "Enter amount to deposit:")
    if amount is None:
        return

    if amount < 0:
        messagebox.showerror("Error", "Invalid amount")
        return

    balance = get_balance()
    balance += amount
    update_balance(balance)
    messagebox.showinfo("Success", "Deposit successful")

def withdraw():
    amount = simpledialog.askfloat("Withdraw", "Enter amount to withdraw:")
    if amount is None:
        return

    balance = get_balance()

    if amount > balance[0]:
        messagebox.showerror("Error", "Insufficient funds")
        return

    if amount < 0:
        messagebox.showerror("Error", "Amount must be greater than 0")
        return

    balance -= amount
    update_balance(balance)
    messagebox.showinfo("Success", "Withdrawal successful")

root = tk.Tk()
root.title("Banking Program")
root.geometry("300x250")

title = tk.Label(root, text="Banking Program", font=("Arial", 16))
title.pack(pady=10)

btn1 = tk.Button(root, text="Show Balance", width=20, command=show_balance)
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Deposit", width=20, command=deposit)
btn2.pack(pady=5)

btn3 = tk.Button(root, text="Withdraw", width=20, command=withdraw)
btn3.pack(pady=5)

btn4 = tk.Button(root, text="Exit", width=20, command=root.destroy)
btn4.pack(pady=5)

root.mainloop()

cursor.close()
conn.close()
