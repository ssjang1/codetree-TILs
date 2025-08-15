n = int(input())
# students = [
#     (h, w, i + 1)
#     for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
# ]

# Please write your code here.

class Student:
    def __init__(self, h, w, n):
        self.h, self.w, self.n, = h,w,n

students = [Student(h,w,i+1) for i,(h,w) in enumerate([tuple(map(int,input().split())) for _ in range(n)])]

students.sort(key = lambda x: (x.h,-x.w))

for s in students:
    print(s.h,s.w,s.n,sep=' ')