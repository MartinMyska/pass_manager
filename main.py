import tkinter as tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #




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
generate_password_button = tk.Button(text="Generate Password", width=12)
add_button = tk.Button(text="Add", width=35)
generate_password_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
