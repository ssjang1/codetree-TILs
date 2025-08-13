n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Please write your code here.

class student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

students = [student(n,k,e,m) for n,k,e,m in zip(name,korean,english,math)]

students.sort(key=lambda x:(-x.kor,-x.eng,-x.math))

for s in students:
    print(s.name, s.kor, s.eng, s.math, sep=' ')