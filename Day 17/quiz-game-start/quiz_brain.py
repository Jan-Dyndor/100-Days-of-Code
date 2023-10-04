# TODO: 1. asking user the questions 2. Chechking if the answer was correct 3. Checking if we are the end of the quiz

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True\False)? ")
        # input(f"Q {self.question_number} {self.question_list[self.question_number].text} (True\False?)").lower()
        self.check_answer(user_answer, current_question.answer)


    def sitll_has_questions(self):
        return self.question_number <= len(self.question_list) - 1

    def check_answer(self, user_answer, right_answer):
        if user_answer.lower() == right_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That is wrong! ")
        print(f"Correct answer is {right_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print()