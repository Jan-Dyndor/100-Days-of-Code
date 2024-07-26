from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain ):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Qizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR, )

        self.score_label = Label(text="Score: ", fg="white",  bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some question text", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"),
                                                     width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image,highlightthickness=0, command=self.true_button)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_image = Button(image=false_image, highlightthickness=0, command=self.false_button)
        self.false_image.grid(row=2, column=1)

        self.get_next_question()


        self.window.mainloop()
       # whenever we cereate an object of the class QuizInterface the init function will be called
    # self.variable turns that variable into property that can be accessed anywhere from the class so true_image or false_image
    # does not have that because we will not use it anywhere else

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text= f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text="END")
            self.true_button.config(state="disabled")
            self.false_image.config(state="disabled")



    def true_button(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_button(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if(is_right):
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

