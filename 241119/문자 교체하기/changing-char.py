a,b = input().split(' ')

b_list = list(b)
b_list[0] = a[0]
b_list[1] = a[1]

print(''.join(b_list))