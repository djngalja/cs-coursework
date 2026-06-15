from math import sqrt


class Student:
    def __init__(self, name: str, female: bool):
        self.name = name
        self.female = female
        self.status: str = "In Queue"
        self.finish_time: float = 0.0

class Examiner:
    def __init__(self, name: str, female: bool):
        self.name = name
        self.female = female
        self.student_cnt: int = 0
        self.failed_cnt: int = 0
        self.current_student_id: int = None
        self.work_time: float = 0

class Question:
    PHI: float = (1 + sqrt(5)) / 2

    def __init__(self, question):
        self.question = question
        self.poss_answers = question.split()
        self.correct_cnt: int = 0