import tkinter as tk
import pyperclip
from tkinter import messagebox
from random import choice, randint, shuffle

LABEL_FONT = ("Courier", 12, "bold")

window = tk.Tk()
window.config(pady=50, padx=50, bg="#fff")
window.title("Password manager")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = [choice(letters) for _ in range(randint(8, 10))] + [choice(symbols) for _ in
                                                                        range(randint(2, 4))] + [choice(numbers) for _
                                                                                                 in
                                                                                                 range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
with open("data.txt") as data_file:
    data_info = data_file.read()
data_list = [data_row.split(' | ') for data_row in data_info.split('\n')[0:len(data_info.split('\n')) - 1]]

last_email = data_list[-1][1] if len(data_list) > 0 else ""
data_file.close()


def add_data_handler():
    website_name = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    if len(username.strip()) == 0 or len(password.strip()) == 0:
        messagebox.showinfo("Oops", message="Please don't leave any fields empty")
        return
    is_confirmed = messagebox.askyesno(title=website_name,
                                       message=f"You've entered the following data:\nWebsite: {website_name}\n"
                                               f"Email: {username}\nPassword: {password}\nDo you want to proceed?")
    if is_confirmed:
        with open("data.txt", "a") as data_f:
            data_f.write(f"{website_name} | {username} | {password}\n")
        pyperclip.copy(password)
        entry_website.delete(0, tk.END)
        entry_password.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #
bg_canvas = tk.Canvas(width=200, height=200, bg="#fff", highlightthickness=0)
bg_image = tk.PhotoImage(file="logo.png")
bg_canvas.create_image(100, 100, image=bg_image)
bg_canvas.grid(row=0, column=1)

label_wb = tk.Label(text="Website:", bg="#fff", font=LABEL_FONT)
label_wb.grid(row=1, column=0)
label_wb = tk.Label(text="Email/Username:", bg="#fff", font=LABEL_FONT)
label_wb.grid(row=2, column=0)
label_wb = tk.Label(text="Password:", bg="#fff", font=LABEL_FONT)
label_wb.grid(row=3, column=0)

entry_website = tk.Entry(width=40)
entry_website.focus()
entry_website.grid(row=1, column=1, columnspan=2)

entry_username = tk.Entry(width=40)
entry_username.insert(0, last_email)
entry_username.grid(row=2, column=1, columnspan=2)
entry_password = tk.Entry(width=22)
entry_password.grid(row=3, column=1)

btn_generate_password = tk.Button(text="Generate Password", command=generate_password)
btn_generate_password.grid(row=3, column=2)
btn_add = tk.Button(text="Add", width=36, command=add_data_handler)
btn_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
