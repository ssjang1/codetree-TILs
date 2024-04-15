s = 0
cnt = 0

for i in range(10):
    n = int(input())

    if n>=0 and n<=200:
        cnt += 1
        s += n

print(s, round(s/cnt,1))