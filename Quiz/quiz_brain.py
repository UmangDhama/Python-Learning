from operator import truediv
from tabnanny import check


class QuizBrain():
    def __init__(self,question_list):
        self.question_number=0
        self.question_list=question_list
        self.score=0

    def still_has_questions(self):
        if self.question_number<len(self.question_list):
            return True
        else:
            print("You've completed the Quiz")
            print(f"Your final score is {self.score}/{len(self.question_list)}")
            return False
    def next_question(self):
        curr_ques=self.question_list[self.question_number].text
        correct_answer=self.question_list[self.question_number].answer
        self.question_number+=1
        user_ans=input(f"Q.{self.question_number}: {curr_ques} (True/False): ")
        self.check_answer(user_ans,correct_answer)
    def check_answer(self,user_ans,correct_answer):
        if user_ans.lower()==correct_answer.lower():
            self.score+=1
            print("You got it right!")
        else:
            print("You got it wrong!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")

