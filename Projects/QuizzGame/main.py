from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain
import html

question_bank = []

for question in question_data["results"]:
    question_bank.append(Question(html.unescape(question["question"]),question["correct_answer"]))



quizz_brain = QuizzBrain(question_bank)
while quizz_brain.still_has_questions():
    quizz_brain.next_question()

print("You've completed the quizz !")
print(f"Your final score was: {quizz_brain.score}/{len(question_bank)}")