n = int(input())
points = [(int(i), map(int, input().split())) for i in range(1,n+1)]

# Please write your code here.

class Point:
    def __init__(self, num, x, y):
        self.num = num
        self.x = x
        self.y = y

dots = []
for num,x,y in points:
