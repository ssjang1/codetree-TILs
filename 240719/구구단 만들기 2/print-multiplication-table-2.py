a,b = map(int, input().split(' '))

for i in range(2,8+1,2):
    string =[]
    for j in range(b,a-1,-1):
        string.append(f'{j} * {i} = {j*i}')
    print(' / '.join(string))