is_true = True

for i in range(5):
    n = int(input())
    if n % 3 != 0:
        is_true = False
        break

if is_true:
    print('1')
else:
    print('0')