import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    """Generate a secure random password based on user selection."""
    try:
        length = int(entry_length.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than 0")
            return
        
        characters = ""
        if var_numeric.get():
            characters += string.digits
        if var_uppercase.get():
            characters += string.ascii_uppercase
        if var_lowercase.get():
            characters += string.ascii_lowercase
        if var_alphanumeric.get():
            characters += string.ascii_letters + string.digits
        if var_special.get():
            characters += string.punctuation
        
        if not characters:
            messagebox.showerror("Error", "Please select at least one character type")
            return
        
        password = ''.join(random.choice(characters) for _ in range(length))
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# Create GUI window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

# Label and Entry for password length
tk.Label(root, text="Enter Password Length:").pack(pady=5)
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

# Checkboxes for character types
var_numeric = tk.BooleanVar()
var_uppercase = tk.BooleanVar()
var_lowercase = tk.BooleanVar()
var_alphanumeric = tk.BooleanVar()
var_special = tk.BooleanVar()

tk.Checkbutton(root, text="Include Numbers", variable=var_numeric).pack()
tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_uppercase).pack()
tk.Checkbutton(root, text="Include Lowercase Letters", variable=var_lowercase).pack()
tk.Checkbutton(root, text="Include Alphanumeric", variable=var_alphanumeric).pack()
tk.Checkbutton(root, text="Include Special Symbols", variable=var_special).pack()
tk.Checkbutton(root, text="")

# Button to generate password
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# Entry to display generated password
tk.Label(root, text="Generated Password:").pack(pady=5)
entry_password = tk.Entry(root, width=30)
entry_password.pack(pady=5)

# Run the GUI application
root.mainloop()
