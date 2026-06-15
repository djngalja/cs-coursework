import multiprocessing
import random
import time

# My modules
from my_classes import Student, Examiner, Question


def exam_simulation(examiner: Examiner, ex_id: int, q: multiprocessing.Queue, 
                    questions: list[Question], students: list[Student], 
                    begin_time: float, res_q: multiprocessing.Queue) -> None:
    had_break: bool = False
    while True:
        st_id = q.get()
        if st_id is None:
            break

        break_duration: int = 0
        if (not had_break and time.time() - begin_time >= 30.0):
            break_duration = random.randint(12, 18)
            time.sleep(break_duration)
            had_break = True

        res_msg = {
            "msg_type": "exam_begin",
            "student_id": st_id,
            "examiner_id": ex_id
        }
        res_q.put(res_msg)
        exam_duration: float = random.uniform(len(examiner.name) - 1, len(examiner.name) + 1)
        time.sleep(exam_duration)

        question_ids: list[int] = random.sample(range(len(questions)), 3)
        correct_cnt: int = 0
        correct_questions = []
        for id in question_ids:
            student_answer:str = get_answer(questions[id].poss_answers, 
                                            students[st_id].female)
            correct: list[str] = get_correct_answers(questions[id].poss_answers,
                                                     examiner.female)
            if student_answer in correct:
                correct_cnt += 1
                correct_questions.append(id)

        mood: str = random.choices(["bad", "good", "neutral"], 
                              weights = [1.0/8.0, 1.0/4.0, 5.0/8.0])[0]
        if (mood == "bad" or (mood == "neutral" and correct_cnt < 2)):
            status = "Failed"
        else:
            status = "Passed"
        finish_time = time.time() - begin_time
        res_msg = {
            "msg_type": "exam_end",
            "examiner_id": ex_id,
            "status": status,
            "work_time": finish_time,
            "correct_question_ids": correct_questions
        }
        res_q.put(res_msg)

def process_res_msg(res_q: multiprocessing.Queue, students: list[Student], 
                 questions: list[Question], examiners: list[Examiner]) -> None:
    while not res_q.empty():
        res_msg = res_q.get()
        id_ex = res_msg["examiner_id"]
        if res_msg["msg_type"] == "exam_begin":
            examiners[id_ex].current_student_id = res_msg["student_id"]
        else:
            id_st = examiners[id_ex].current_student_id
            examiners[id_ex].current_student_id = None
            students[id_st].status = res_msg["status"]
            students[id_st].finish_time = res_msg["work_time"]
            for id_q in res_msg["correct_question_ids"]:
                questions[id_q].correct_cnt += 1
            examiners[id_ex].student_cnt += 1
            if res_msg["status"] == "Failed":
                examiners[id_ex].failed_cnt += 1
            examiners[id_ex].work_time = res_msg["work_time"]

# Utility functions
def get_answer(poss_answers: list[str], female: bool) -> str:
    weights: list[float] = [1.0 / Question.PHI]
    for _ in range(len(poss_answers) - 1):
        temp: float = (1.0 - sum(weights)) / Question.PHI
        weights.append(temp)
    if female:
        weights.reverse()
    return random.choices(poss_answers, weights = weights)[0]

def get_correct_answers(poss_answers: list[str], female: bool) -> list[str]:
    answer: str = get_answer(poss_answers, female)
    copy_poss_answers: list[str] = poss_answers.copy()
    copy_poss_answers.remove(answer)
    res: list[str] = [answer]
    while (random.random() < 1.0/3.0 and len(copy_poss_answers) > 0):
        answer = get_answer(copy_poss_answers, female)
        copy_poss_answers.remove(answer)
        res.append(answer)
    return res