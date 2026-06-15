import multiprocessing
import time
import os

# My modules
from get_input import get_students, get_examiners, get_questions
from print_results import print_results, print_current_info
from simulation import exam_simulation, process_res_msg


def main() -> None:
    q = multiprocessing.Queue()
    students = []
    examiners = []
    questions = []
    if (get_students(q, students) and get_examiners(examiners) and get_questions(questions)):
        res_q = multiprocessing.Queue()
        workers = []
        begin_time = time.time()
        for i in range(len(examiners)):
            p = multiprocessing.Process(target=exam_simulation, 
                                        args=(examiners[i], i, q, questions, students, begin_time, res_q))
            workers.append(p)
            p.start()
        for _ in range(len(examiners)):
            q.put(None)
        active_workers = len(workers)
        while active_workers > 0:
            process_res_msg(res_q, students, questions, examiners)
            os.system('cls' if os.name == 'nt' else 'clear')
            print_current_info(students, examiners)
            time.sleep(0.5)
            active_workers = sum(1 for p in workers if p.is_alive())
        process_res_msg(res_q, students, questions, examiners)
        os.system('cls' if os.name == 'nt' else 'clear')
        print_current_info(students, examiners)
        for p in workers:
            p.join()
        os.system('cls' if os.name == 'nt' else 'clear')
        print_results(students, examiners, questions)
    

if __name__ == "__main__":
    main()