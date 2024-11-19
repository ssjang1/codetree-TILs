line = input()

a = list(line)
a.pop(1)
a.pop(-2)

print(''.join(a))