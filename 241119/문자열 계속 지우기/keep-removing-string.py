a = input()
b = input()

while True:
    if b in a:
        point = a.index(b)
        a = a[:point] + a[point+2:]
    else:
        break
print(a)