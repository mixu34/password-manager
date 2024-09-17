import tkinter as tk
import pyperclip
from tkinter import messagebox
from password_saver import PasswordSaver
from password_generator import PasswordGenerator


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    entry_password.delete(0, tk.END)
    generated_password = PasswordGenerator().generate_random_password()
    entry_password.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    if not website:
        messagebox.showwarning(title="Error", message="Field 'Website' can't be null")
    elif not email:
        messagebox.showwarning(title="Error", message="Field 'Email/Username' can't be null")
    elif not password:
        messagebox.showwarning(title="Error", message="Field 'Password' can't be null")
    else:
        new_password = PasswordSaver(website, email, password)
        if new_password.check_if_website_not_in_file():
            new_password.save_password()
            entry_website.delete(0, tk.END)
            entry_password.delete(0, tk.END)
            messagebox.showinfo(title="Success", message=f"Credentials for {website} added.")
        else:
            is_ok = messagebox.askokcancel(title="Website found!",
                                           message="Do you want to change existing credentials for this site?")
            if is_ok:
                new_password.save_password()
                entry_website.delete(0, tk.END)
                entry_password.delete(0, tk.END)


def search_website():
    website = entry_website.get()
    data = PasswordSaver()
    find_result = PasswordSaver.get_password(data, website)
    print(type(find_result))
    if isinstance(find_result, dict):
        message = f"Email: {find_result["email"]}\nPassword: {find_result["password"]}"
    else:
        message = find_result
    messagebox.showinfo(title=website, message=message)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password generator")
window.config(padx=40, pady=40)

canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1, padx=2, pady=2)

label_website = tk.Label(text="Website:")
label_website.grid(row=1, column=0, sticky="E", padx=2, pady=2)
label_email = tk.Label(text="Email/Username:")
label_email.grid(row=2, column=0, sticky="E", padx=2, pady=2)
label_password = tk.Label(text="Password:")
label_password.grid(row=3, column=0, sticky="E", padx=2, pady=2)

entry_website = tk.Entry(width=21)
entry_website.grid(row=1, column=1, sticky="EW", padx=2, pady=2)
entry_website.focus()
entry_email = tk.Entry(width=35)
entry_email.grid(row=2, column=1, columnspan=2, sticky="EW", padx=2, pady=2)
entry_email.insert(0, "je.mateusz.morawiecki@gov.pl")
entry_password = tk.Entry(width=21)
entry_password.grid(row=3, column=1, sticky="EW", padx=2, pady=2)

button_search = tk.Button(text="Search", command=search_website)
button_search.grid(row=1, column=2, sticky="EW", padx=2, pady=2)
button_generate = tk.Button(text="Generate Password", command=generate_password)
button_generate.grid(row=3, column=2, sticky="EW", padx=2, pady=2)
button_add = tk.Button(text="Add", width=36, command=add_password)
button_add.grid(row=4, column=1, columnspan=2, sticky="EW", padx=2, pady=2)

window.mainloop()
