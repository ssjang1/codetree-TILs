n = int(input())
# name = []
# height = []
# weight = []
people = []

class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

for _ in range(n):
    n_i, h_i, w_i = input().split()
    # name.append(n_i)
    # height.append(int(h_i))
    # weight.append(int(w_i))
    people.append(Person(n_i, int(h_i), int(w_i)))

people.sort(lambda x: (x.height, -x.weight))
for p in people:
    print(p.name, p.height, p.weight, sep=' ')
