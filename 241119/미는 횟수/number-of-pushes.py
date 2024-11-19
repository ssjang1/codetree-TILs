A = input()
B = input()

cnt = 0
while True:
    if A == B:
        print(cnt)
        break
    else:
        if cnt >=len(A)-1:
            print(-1)
            break
        A = A[-1] + A[:-1]
        cnt+=1
