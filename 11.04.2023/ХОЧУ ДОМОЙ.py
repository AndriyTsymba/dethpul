'''
import random
marks = [random.randint(40, 100) for i in range(3)]
students = {"vitalya": [random.randint(40, 100) for i in range(3)],
           "nastya": [random.randint(40, 100) for i in range(3)],
            "zhenyagleb": [random.randint(40, 100) for i in range(3)]}
print(students)
total=0
for student, marks, in students.items():
    total= sum([i for i in marks])
    print(round(total/len(marks)))
'''
#poshuk odnakowyh sumvoliv
row={}
string=input()
for i in string:
    if i in row:
        row[i]+=1
    else:
        row[i]=1
for i in row:
    print(i, row[i])
print(row)