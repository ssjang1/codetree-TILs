A = input()

total = 0

for a in A:
    if a.isdigit():
        total+=int(a)

print(total)