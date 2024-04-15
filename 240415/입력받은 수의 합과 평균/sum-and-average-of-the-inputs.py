n = int(input())

s = 0
cnt = 0

for i in range(n):
    a = int(input())
    s += a
    cnt += 1

print(s, round(s/cnt,1))