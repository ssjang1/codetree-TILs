a_mat, a_eng = map(int, input().split(' '))
b_mat, b_eng = map(int, input().split(' '))

if a_mat==b_mat :
    if a_eng>b_eng:
        print('A')
    else:
        print('B')
else:
    if a_mat>b_mat:
        print('A')
    else:
        print('B')