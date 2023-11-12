from tkinter import *


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

def button_clicked():
    # my_label["text"] = "Button was clicked!"
    new_text = input.get()
    my_label.config(text=new_text)


# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold "))
# Putting Label into a screen center
# my_label["text"]="Kitty"
# my_label.config(text="test2")

# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

button2 = Button(text="New Button")
button2.grid(column=2, row=0)

#  Entry component
input = Entry(width=20)
i = input.get()
# input.pack()
input.grid(column= 3, row=2)




window.mainloop()

