N = input()

# Please write your code here.

binary = list(map(int, N))

num = 0

for i in range(len(binary)):
    num = num*2 + binary[i]

num17 = num * 17

digits = []

while True:
    if num17 < 2:
        digits.append(num17)
        break
    
    digits.append(num17 % 2)
    num17 //= 2

for d in digits[::-1]:
    print(d,end='')