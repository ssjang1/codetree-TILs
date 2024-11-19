line1 = input()
line2 = input()

if line2 in line1:
    print(line1.index(line2))
else:
    print(-1)