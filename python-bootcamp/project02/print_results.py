from prettytable import PrettyTable

# My modules
from my_classes import Student, Examiner, Question


def print_current_info(students: list[Student], examiners: list[Examiner]) -> None:
    print_current_student_table(students)
    print_current_examiner_table(students, examiners)
    in_queue_cnt = sum(1 for st in students if st.status == "In Queue")
    print(f"Remaining in queue: {in_queue_cnt} out of {len(students)}")
    ttl_duration = max(ex.work_time for ex in examiners)
    print(f"Time since exam started: {ttl_duration:.2f}")

def print_results(students: list[Student], examiners: list[Examiner], questions: list[Question]) -> None:
    print_final_student_table(students)
    print_final_examiner_table(examiners)
    ttl_duration = max(ex.work_time for ex in examiners)
    print(f"Time from exam start to finish: {ttl_duration:.2f}")
    print_top_students(students)
    print_top_examiners(examiners)
    print_expelled(students)
    print_best_questions(questions)
    ttl_st_passed = sum(1 for st in  students if st.status == "Passed")
    final_res = "passed" if float(ttl_st_passed) / len(students) > 0.85 else "failed"
    print(f"Result: Exam {final_res}")

# Utility functions
def print_current_student_table(students: list[Student]) -> None:
    status_priority = {
        "In Queue": 0,
        "Passed": 1,
        "Failed": 2
    }
    students_srt = sorted(students, key=lambda student: status_priority[student.status])
    student_Table = PrettyTable(["Student", "Status"])
    for student in students_srt:
        student_Table.add_row([student.name, student.status])
    print(student_Table)

def print_current_examiner_table(students: list[Student], examiners: list[Examiner]) -> None:
    examiner_Table = PrettyTable(["Examiner", "Current Student", "Total Students", "Failed", "Work Time"])
    examiner_Table.float_format = '.2'
    for examiner in examiners:
        student_name = "-" if examiner.current_student_id == None else students[examiner.current_student_id].name
        examiner_Table.add_row([examiner.name, student_name, examiner.student_cnt, examiner.failed_cnt, examiner.work_time])
    print(examiner_Table)

def print_final_student_table(students: list[Student]) -> None:
    students_srt = sorted(students, key=lambda student: student.status, reverse=True)
    student_Table = PrettyTable(["Student", "Status"])
    for student in students_srt:
        student_Table.add_row([student.name, student.status])
    print(student_Table)

def print_final_examiner_table(examiners: list[Examiner]) -> None:
    examiner_Table = PrettyTable(["Examiner", "Total Students", "Failed", "Work Time"])
    examiner_Table.float_format = '.2'
    for examiner in examiners:
        examiner_Table.add_row([examiner.name, examiner.student_cnt, examiner.failed_cnt, examiner.work_time])
    print(examiner_Table)

def print_top_students(students: list[Student]) -> None:
    passed = [s for s in students if s.status == "Passed"]
    if passed:
        fastest_time = min(s.finish_time for s in passed)
        fastest_passed = [s.name for s in passed if s.finish_time == fastest_time]
        fastest_passed_str = ", ".join(fastest_passed)
    else:
        fastest_passed_str = ""
    print(f"Top-performing students: {fastest_passed_str}")

def print_top_examiners(examiners: list[Examiner]) -> None:
    lowest_falure_rate = min(ex.failed_cnt for ex in examiners)
    top_examiners = [ex.name for ex in examiners if ex.failed_cnt == lowest_falure_rate]
    top_examiners_str = ", ".join(top_examiners)
    print(f"Top examiners: {top_examiners_str}")

def print_expelled(students: list[Student]) -> None:
    failed = [s for s in students if s.status == "Failed"]
    if failed:
        fastest_time = min(s.finish_time for s in failed)
        fastest_failed = [s.name for s in failed if s.finish_time == fastest_time]
        fastest_failed_str = ", ".join(fastest_failed)
    else:
        fastest_failed_str = ""
    print(f"Students to be expelled: {fastest_failed_str}")

def print_best_questions(questions: list[Question]) -> None:
    best_rate = max(q.correct_cnt for q in questions)
    best_questions = [q.question for q in questions if q.correct_cnt == best_rate]
    best_questiong_str = ", ".join(best_questions)
    print(f"Best questions: {best_questiong_str}")