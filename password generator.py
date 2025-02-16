import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# Function to copy password to clipboard
def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Password copied to clipboard")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x250")
root.configure(bg="#f4f4f4")

# Widgets
tk.Label(root, text="Enter Password Length:", bg="#f4f4f4").pack(pady=5)
length_entry = tk.Entry(root, width=10)
length_entry.pack()

tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white").pack(pady=10)

password_entry = tk.Entry(root, width=30)
password_entry.pack()

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#008CBA", fg="white").pack(pady=10)

# Run the application
root.mainloop()
