n, A = input().strip().split(' ')
n = int(n)
cnt = 0
for i in range(n):
    word = input()
    if A == word:
        cnt +=1
print(cnt)