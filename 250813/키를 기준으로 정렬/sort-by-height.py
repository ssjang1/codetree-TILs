n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.

class person:
    def __init__(self, name, height, weight):
        self.n = name
        self.h = height
        self.w = weight

people = [person(n,h,w) for n,h,w in zip(name,height,weight)]

people.sort(key= lambda x: x.h)

for p in people:
    print(p.n, p.h, p.w, sep=' ')
