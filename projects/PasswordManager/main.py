from tkinter import messagebox
import tkinter
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    entry_password.delete(0, tkinter.END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    if len(entry_website.get()) == 0 or len(entry_password.get()) == 0:
        messagebox.showinfo(title="Oops, something went wrong...", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=entry_website.get(),
                                       message=f"These are the details entered: \nE-mail: {entry_user.get()}"
                                               f"\nPassword: {entry_password.get()}\nIs it ok to save?")

        if is_ok:
            new_data = {
                entry_website.get(): {
                    "email": entry_user.get(),
                    "password": entry_password.get()
                }
            }
            try:
                with open("./data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("./data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                entry_website.delete(0, tkinter.END)
                entry_password.delete(0, tkinter.END)


# ------------------------- FIND PASSWORD ---------------------------- #
def find_password():
    website = entry_website.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, width=300, height=300)

logo = tkinter.PhotoImage(file="PasswordManager/logo.png")

canvas = tkinter.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

button_gen_pass = tkinter.Button(text="Generate Password", command=generate_password)
button_gen_pass.grid(row=3, column=2)

button_add = tkinter.Button(text="Add", command=add, width=42)
button_add.grid(row=4, column=1, columnspan=2)

button_search = tkinter.Button(text="Search", width=15, command=find_password)
button_search.grid(row=1, column=2)

label_website = tkinter.Label(text="Website:")
label_website.grid(row=1, column=0)
label_user = tkinter.Label(text="E-mail/Username:")
label_user.grid(row=2, column=0)
label_password = tkinter.Label(text="Password:")
label_password.grid(row=3, column=0)

entry_website = tkinter.Entry(width=32)
entry_website.grid(row=1, column=1)
entry_website.focus()
entry_user = tkinter.Entry(width=50)
entry_user.grid(row=2, column=1, columnspan=2)
entry_user.insert(0, "kesleyraimundo@gmail.com")
entry_password = tkinter.Entry(width=32)
entry_password.grid(row=3, column=1)

window.mainloop()
