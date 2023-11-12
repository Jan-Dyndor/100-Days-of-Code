from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)


def calculate():
    miles = float(entry.get())
    km = 1.609344 * miles
    km_rounded = round(km, 2)
    result_of_conversion_label.config(text=km_rounded)


entry = Entry()
entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

result_of_conversion_label = Label(text=0)
result_of_conversion_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row = 1)

calc_button = Button(text="Calculate", command=calculate)
calc_button.grid(column=1, row=2)














window.mainloop()