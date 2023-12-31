from tkinter import *
from tkinter import messagebox
import random
# copy the password instantly after its generated
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)] + [random.choice(symbols) for symbol in range(nr_symbols)] + [random.choice(numbers) for number in range(nr_numbers)]
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    password_ent.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = web_ent.get()
    email = user_ent.get()
    password = password_ent.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Do not leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: "
                                       f"\n email:{email} \n password: {password} \n Is it OK to save?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
            web_ent.delete(0, END)
            user_ent.delete(0, END)
            password_ent.delete(0, END)
            user_ent.insert(END, "example@email.com")



# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password")
window.minsize(width=200, height=200)
window.config(padx=70, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0, columnspan=2)

web_label = Label(text="Website:")
web_label.grid(column=0, row=1, sticky="e")


web_ent = Entry(width=43)
web_ent.grid(column=1, row=1, columnspan=2, sticky="w")
web_ent.focus()


user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2, sticky="e")

user_ent = Entry(width=43)
user_ent.grid(column=1, row=2, columnspan=2, sticky="w")
user_ent.insert(END, "example@email.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="e")


password_ent = Entry(width=22)
password_ent.grid(column=1, row=3)


gen_pass_btn = Button(text="Generate Password", command=gen_password)
gen_pass_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=36, command=save_data)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
