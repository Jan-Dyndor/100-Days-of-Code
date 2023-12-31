from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    q = Question(question["question"], question["correct_answer"])
    question_bank.append(q)

# print(question_bank[0].text)
quiz = QuizBrain(question_bank)
while quiz.sitll_has_questions():
    quiz.next_question()
print("You have completed the quiz!")
print(f"Your final score is {quiz.score}\{quiz.question_number}")