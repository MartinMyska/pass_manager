import tkinter as tk
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    pass_char = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    pass_number = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = pass_char + pass_letters + pass_number
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email, "password": password}}

    if not (website and password):
        messagebox.showinfo(title="Whoops", message="Please fill in the fields")
        return

    with open("data.json", "r") as f:
        data = json.load(f)
        data.update(new_data)

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

    print(data)
    website_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = tk.Canvas(height=220, width=220)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = tk.Label(text="Website:")
email_label = tk.Label(text="Email/Username:")
password_label = tk.Label(text="Password:")
website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

# Entries
website_entry = tk.Entry(width=35)
email_entry = tk.Entry(width=35)
password_entry = tk.Entry(width=19)
website_entry.grid(row=1, column=1, columnspan=2)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)
website_entry.focus()
email_entry.insert(0, "martin.mysska@gmail.com")

# Buttons
generate_password_button = tk.Button(text="Generate Password", width=12, command=generate_password)
add_button = tk.Button(text="Add", width=35, command=save)
generate_password_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
