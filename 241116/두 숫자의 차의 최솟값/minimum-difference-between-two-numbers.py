n = int(input())
line = list(map(int,input().strip().split(' ')))
import sys
mini = sys.maxsize

for i in range(len(line)):
    for j in range(i+1,len(line)):
        value = abs(line[i]-line[j])
        if value < mini:
            mini = value

print(mini)
