import random

def main():
    students={'Matt Stony':{'math':0, 'science':0, 'english':0, 'history':0, 'coding':0},
    'Nikolina Ben':{'math':0, 'science':0, 'english':0, 'history':0, 'coding':0},
    'Komang Paula':{'math':0, 'science':0 ,'english':0, 'history':0, 'coding':0},
    'Kyle Renata':{'math':0, 'science':0, 'english':0, 'history':0, 'coding':0},
    'Carmen Candida':{'math':0, 'science':0, 'english':0, 'history':0, 'coding':0},
    'John Smith':{'math':0, 'science':0, 'english':0, 'history':0, 'coding':0},
    'Sneh Patel':{'math':0, 'science':0,'english':0, 'history':0, 'coding':0},
    'Randy Rom':{'math':0, 'science':0,'english':0, 'history':0, 'coding':0}}

    averages = {}

    init_marks(students)
    get_averages(students, averages)
    print_marks(students, averages)

def init_marks(students):
    for student, marks in students.items():
        for sub, mark in marks.items():
            mark = random.randint(50,100)
            students[student][sub] = mark

def get_averages(students, averages):
    for student, marks in students.items():
        averages[student] = sum(marks.values())/len(marks) 

def print_marks(students, averages):    

    print('Class Report Card:')
    for student, marks in students.items():
        print(student, marks)

    print('\nAverages')
    for student, avg_marks in averages.items():
        print(student + "'s average marks:", avg_marks)

 

main()


