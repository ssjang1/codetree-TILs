n = int(input())

def number_suare(n):
    start = 1
    for i in range(n):
        for j in range(n):
            print(start,end=' ')
            if start ==9:
                start=0
            start +=1
        print()
number_suare(n)