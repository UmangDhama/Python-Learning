from data import question_data
from  question_model import Question
from  quiz_brain import QuizBrain

question_bank=[]

for ques in question_data:
    Ques=Question(ques["text"],ques["answer"])
    question_bank.append(Ques)

print(question_bank)

Quiz=QuizBrain(question_bank)
while Quiz.still_has_questions():
    Quiz.next_question()