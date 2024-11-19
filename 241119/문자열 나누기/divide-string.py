n = int(input())
words = input().strip().split(' ')

line =''
for w in words:
    line += w

for i in range(len(line)//5 +1):
    print(line[5*i:5+5*i])