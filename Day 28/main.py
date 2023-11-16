from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repeat = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", bg=YELLOW, fg=GREEN)
    canvas.itemconfig(time_text, text="00:00")
    check_mark.config(text="")
    # # To change global variable we will use a global keyword, if we didnt Pythn would create a repeat # variable
    # in function scope so we will not change a global variable
    global repeat
    repeat = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global repeat
    repeat += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if repeat % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif repeat % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # Dynamic typing - change variable type from number to string
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        # Timer goes to 0 and we call start_timer() to immediately go to work or break session
        start_timer()
        # Every work-break session add ✔
        marks = ""
        work_sessions = math.floor(repeat/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

# Create a Canvas Widget to display a tomato photo
canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
# PhotoImage class is required to read through a file and get hold of a img
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row =1)


start_btn = Button(text="Start", highlightthickness = 0, command = start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

check_mark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25, "bold"))
check_mark.grid(column=1, row =3)

window.mainloop()

