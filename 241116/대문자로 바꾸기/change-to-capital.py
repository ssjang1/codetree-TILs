for i in range(5):
    line = input().split(' ')
    changed_line = [x.upper() for x in line ]
    for j in changed_line:
        print(j, end=" ")
    print()