a = 19

for i in range(1,a+1):
    for j in range(1,a+1):
        if j ==19:
            print(f'{i} * {j} = {i*j}')
        elif j %2 ==1:
            print(f'{i} * {j} = {i*j}',end=' / ')
        else:
            print(f'{i} * {j} = {i*j}')