a, b = map(int, input().split())
n = input()

# Please write your code here.

binary = list(map(int,n))

num = 0

for i in range(len(binary)):
    num = num * a + binary[i]

digits = []

while True:
    if num < b:
        digits.append(num)
        break
    
    digits.append(num % b)
    num //= b

for d in digits[::-1]:
    print(d,end='')