n3 , n5 = 0, 0

for i in range(10):
    num = int(input())
    if num % 3 == 0:
        n3 += 1
    if num % 5 == 0:
        n5 += 1

print(n3, n5, sep=' ')