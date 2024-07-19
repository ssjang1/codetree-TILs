n = int(input())

for i in range(n):
    string =''
    # string.append(' '*i)
    string += ' '*i
    for j in range(n-i):
        # string.append(n-j)
        string += str(n-j -i)
    print(' '.join(string))