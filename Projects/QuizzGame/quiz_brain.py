class QuizzBrain:
    question_number:int 
    question_list:list
    score:int

    def __init__(self,question_list):
        self.question_number=0
        self.question_list=question_list
        self.score=0

    def next_question(self):
        curent_question = self.question_list[self.question_number]
        self.question_number+=1
        user_answer = input(f"Q.{self.question_number}: {curent_question.text} (True/False)?: ")
        self.check_answer(user_answer,curent_question.answer)
    
    def still_has_questions(self):
        return len(self.question_list)>self.question_number
    
    def check_answer(self,user_answer,correct_answer):
        if(user_answer.strip().title()==correct_answer):
            print("You got it right")
            self.score+=1
        else:
            print("That's wrong")
            print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is:{self.score}/{self.question_number}")
        print("\n")
        