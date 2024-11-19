a = input()
b = input()
b_len = len(b)
while True:
    if b in a:
        point = a.index(b)
        a = a[:point] + a[point+b_len:]
    else:
        break
print(a)