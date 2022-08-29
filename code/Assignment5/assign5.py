import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
myfont = font_manager.FontProperties(fname="C:\\WINDOWS\\Fonts\\simsun.ttc", size=14)
def string_to_float(s):
    try:
        return float(s)
    except ValueError:
        return 0
def autolabel(rect1,rect2):
    for i in range(len(rect1)):
        h1 = rect1[i].get_height() if rect1[i].get_height() is not None else 0
        h2 = rect2[i].get_height() if rect2[i].get_height() is not None else 0
        height = h1+h2
        plt.text(rect1[i].get_x() + rect1[i].get_width() / 2. - 0.25, 1.01 * rect1[i].get_height(), '%.2f' % float(rect1[i].get_height()/height))


data_csv = pd.read_csv('data.csv',low_memory=False)
problems = data_csv['Problem Name']
durations = data_csv['Duration (sec)']
students = data_csv['Anon Student Id']
index = 0
problem_duration = dict()
print(problems[0])
for index in range(len(problems)):
    if problems[index] in problem_duration.keys():
       problem_duration[problems[index]] += string_to_float(durations[index])
    else:
        problem_duration[problems[index]] = string_to_float(durations[index])
print(problem_duration)


problem_level = data_csv['Level (ProblemSet)']
response = data_csv['Student Response Type']
correctness = data_csv['Outcome']

problem_level_response = {}
for index in range(len(problems)):
    if problem_level[index] in problem_level_response.keys():
       if response[index] == 'HINT_REQUEST':
           problem_level_response[problem_level[index]] += 1
    else:
        if response[index] == 'HINT_REQUEST':
            problem_level_response[problem_level[index]]=1
        else:
            problem_level_response[problem_level[index]]=0

list_hint = []
# A plot showing the number of hints requested by students
# on each problem level.
x = []
for i in problem_level_response.keys() :
    list_hint.append(problem_level_response.get(i))
    x.append(i)
print(problem_level_response)
plt.figure(figsize=(30,10),dpi=60)
plt.xticks(rotation=90, fontsize=14)
plt.bar(x, list_hint, width=0.8, color="blue")
plt.ylabel('hint_request_times')
plt.xlabel('problem_level')
# plt.savefig('hint_times.png')
plt.show()

list_duration = []
# A histogram of the time students spends on any given problem.
x = []
for i in problem_duration.keys() :
    list_duration.append(problem_duration.get(i))
    x.append(i)
plt.figure(figsize=(30,10),dpi=80)
plt.xticks(rotation=90, fontsize=14)
plt.bar(x, list_duration, width=0.8, color="blue")
plt.ylabel('duration(sec)')
plt.xlabel('problem_no')
# plt.savefig('problems_duration.png')
plt.show()

# Correctness of each student's attempt
student_correct_dict = {}
student_incorrect_dict = {}
for i in range(len(students)):
        if correctness[i]=='CORRECT':
            if students[i] in student_correct_dict.keys():
                student_correct_dict[students[i]] += 1
            else:
                student_correct_dict[students[i]] = 1
        else:
            if students[i] in student_incorrect_dict.keys():
                student_incorrect_dict[students[i]] += 1
            else:
                student_incorrect_dict[students[i]] = 1
print(student_correct_dict)
print(student_incorrect_dict)
correct_y = list()
incorrect_y = list()
x ={}
for i in student_correct_dict.keys():
    correct_y.append(student_correct_dict.get(i))
    incorrect_y.append(student_incorrect_dict.get(i))
    x[i] = i
plt.figure(figsize=(20,8),dpi=80)
a = plt.bar(range(len(x)), correct_y, width=0.5, color="green",label='Correct Attempts')
b = plt.bar(range(len(x)), incorrect_y, width=0.5, color="red",label='Incorrect Attempts')
plt.xticks(range(len(x)))
plt.legend(loc="upper right")
plt.xlabel("Student Id.", fontproperties=myfont)
plt.ylabel("Correct/Incorrect Attempts", fontproperties=myfont)
autolabel(a,b)
plt.savefig('correctness of students')

plt.show()
# Correctness of each question

problems_correct_dict = {}
problems_incorrect_dict = {}
for i in range(len(problems)):
        if correctness[i]=='CORRECT':
            if problems[i] in problems_correct_dict.keys():
                problems_correct_dict[problems[i]] += 1
            else:
                problems_correct_dict[problems[i]] = 1
        else:
            if problems[i] in problems_incorrect_dict.keys():
                problems_incorrect_dict[problems[i]] += 1
            else:
                problems_incorrect_dict[problems[i]] = 1
print(problems_correct_dict)
print(problems_incorrect_dict)
correct_y = list()
incorrect_y = list()
x ={}
for i in problems_correct_dict.keys():
    correct_y.append(problems_correct_dict.get(i))
    if problems_incorrect_dict.get(i) is None:
        incorrect_y.append(0)
    else:
        incorrect_y.append(problems_incorrect_dict.get(i))
    x[i] = i
plt.figure(figsize=(20,8),dpi=80)
a = plt.bar(range(len(x)), correct_y, width=0.5, color="green",label='Correct Attempts')
b = plt.bar(range(len(x)), incorrect_y, width=0.5, color="red",label='Incorrect Attempts')
plt.xticks(range(len(x)))
plt.legend(loc="upper right")
autolabel(a,b)
plt.xlabel("Problem Name.", fontproperties=myfont)
plt.ylabel("Correct/Incorrect Attempts", fontproperties=myfont)
plt.savefig('correctness of problems')
plt.show()