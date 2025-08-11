MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.
class agent:
    def __init__(self, codename='', score=0):
        self.codename = codename
        self.score = score

agents = []

for a,b in zip(codenames, scores):
    agents.append(agent(a,b))

check = 101
name = ''
for i in range(MAX_N):
    if agents[i].score < check:
        check = agents[i].score
        name = agents[i].codename

print(f'{name} {check}')