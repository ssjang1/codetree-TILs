line = input()

char1 = line[0]
char2 = line[1]

result = ''

for i in line:
    if i == char1:
        result+=char2
    elif i == char2:
        result+=char1
    else:
        result+=i

print(result)