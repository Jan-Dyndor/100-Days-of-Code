from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2, sticky="e")

user_ent = Entry(width=43)
user_ent.grid(column=1, row=2, columnspan=2, sticky="w")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="e")

password_ent = Entry(width=22)
password_ent.grid(column=1, row=3)

gen_pass_btn = Button(text="Generate Password")
gen_pass_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=36)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
