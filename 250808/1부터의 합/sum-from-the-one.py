N = int(input())

s=0

for i in range(1,101,1):
    s+=i
    if s>=N:
        print(i)
        break