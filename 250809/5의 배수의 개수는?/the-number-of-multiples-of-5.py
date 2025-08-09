arr = [list(map(int,input().strip().split(' '))) for _ in range(4)]

cnt = 0

for row in arr:
    for elem in row:
        if elem %5 ==0:
            cnt += 1

print(cnt)