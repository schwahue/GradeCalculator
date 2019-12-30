def main():
    s = Grade()
    print(s)


class Grade:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.score = 0
        self.total_score = 0
        self.grade = ""
        self.get_score()
        self.cal_score()
        self.get_grade()

    def get_score(self):
        self.x = int(input("Enter your score: "))
        self.y = int(input("Enter the test total score: "))
        self.z = int(input("Enter the test percentage: "))
        self.score = (self.x / self.y) * 100

    def cal_score(self):
        self.total_score = (self.score * self.z) / 100

    def get_grade(self):
        if self.score > 80:
            self.grade = "A"
        elif self.score > 70:
            self.grade = "B"
        elif self.score > 60:
            self.grade = "C"
        elif self.score > 50:
            self.grade = "D"
        else:
            self.grade = "F"

    def __str__(self):
        msg = f"Your score is {self.score}. \n" \
              f"Your total score is {self.total_score}. \n" \
              f"Your grade is {self.grade}."
        return msg

main()
