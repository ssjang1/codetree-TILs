n = int(input())

def result(n):
    if n ==1:
        return 1
    if n==2:
        return 2
    return result(n-2) + n 

print(result(n))