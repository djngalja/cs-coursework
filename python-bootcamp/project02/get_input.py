import os
import multiprocessing

# My modules
from my_classes import Student, Examiner, Question


def get_students(q: multiprocessing.Queue, students: list[Student]) -> bool:
    try:
        f_name: str = "students.txt"
        f_sz: int = os.path.getsize(f_name)
        if f_sz == 0:
            raise ValueError
        student_id: int  = 0
        with open(f_name, "r") as file:
            for line in file:
                if line.strip():
                    name, female = get_person_info(line)
                    students.append(Student(name, female))
                    q.put(student_id)
                    student_id += 1
        return True
    except ValueError:
        print(f"Error: invalid input - {f_name}")
        return False
    except FileNotFoundError:
        print(f"Error: {f_name} not found")
        return False

def get_examiners(examiners: list[Examiner]) -> bool:
    try:
        f_name: str = "examiners.txt"
        f_sz: int = os.path.getsize(f_name)
        if f_sz == 0:
            raise ValueError
        with open(f_name, "r") as file:
            for line in file:
                if line.strip():
                    name, female = get_person_info(line)
                    examiners.append(Examiner(name, female))
        return True
    except ValueError:
        print(f"Error: invalid input - {f_name}")
        return False
    except FileNotFoundError:
        print(f"Error: {f_name} not found")
        return False

def get_questions(questions: list[Question]) -> bool:
    try:
        f_name: str = "questions.txt"
        f_sz: int = os.path.getsize(f_name)
        if f_sz == 0:
            raise ValueError
        with open(f_name, "r") as file:
            for line in file:
                if line.strip():
                    question = line.strip()
                    questions.append(Question(question))
        return True
    except ValueError:
        print(f"Error: invalid input - {f_name}")
        return False
    except FileNotFoundError:
        print(f"Error: {f_name} not found")
        return False

# Utility functions
def get_person_info(line: str) -> tuple[str, bool]:
    name, gender = line.split()
    if (gender != "F" and gender != "M"):
        raise ValueError
    female: bool = True if gender == "F" else False
    return name, female