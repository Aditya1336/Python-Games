class QuizBrain:
    def __init__(self,obj_list):
        self.current_question = 0
        self.question_list = obj_list
        self.points = 0

    def next_question(self):
        ans = input(f"Q.{self.current_question+1}  {self.question_list[self.current_question].text} (True/False): ")
        if ans == self.question_list[self.current_question].answer:
            self.points+=1
            print(f"Correct! Score: {self.points}/{self.current_question+1} ")
        else:
            print(f"Incorrect! Score : {self.points}/{self.current_question+1}")
        print("\n")
        self.current_question+=1

