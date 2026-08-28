from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)
print(question_bank)

while quiz_brain.still_has_question():
    quiz_brain.next_question()
    print("\n")

print("You have completed the quiz.")
print(f"Your total score is: {quiz_brain.user_score}/{quiz_brain.question_number}.")






