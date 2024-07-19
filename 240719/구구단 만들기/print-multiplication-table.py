a,b = map(int, input().split())

for i in range(1,10):
    string =[]  
    for j in range(b,a-1,-2):
        string.append(f'{j} * {i} = {j*i}')
    print(' / '.join(string))