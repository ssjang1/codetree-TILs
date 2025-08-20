n = int(input())

# Please write your code here.

num_2 = []
while True:
    if n<2:
        num_2.append(n)
        break
    num_2.append(n%2)
    n //= 2

for i in num_2[::-1]:
    print(i, end='')
