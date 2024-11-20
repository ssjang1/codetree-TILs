n = int(input())

def answer(arr):
    new_arr = []
    for a in arr:
        if a%2 == 0:
            a /= 2
        new_arr.append(a)
    
    for b in new_arr:
        print(int(b),end=' ')

arr = list(map(int,input().strip().split(' ')))
answer(arr)