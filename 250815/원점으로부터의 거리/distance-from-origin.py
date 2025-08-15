n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(1,n+1)]

# Please write your code here.

class Point:
    def __init__(self, num, x, y):
        self.num = num
        self.x = x
        self.y = y

dots = []
for num, (x,y) in points:
    dots.append(Point(num,x,y))

dots.sort(key = lambda x: (abs(x.x)+abs(x.y),x.num))

for d in dots:
    print(d.num)