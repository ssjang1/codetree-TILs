w1, w2 = input().strip().split(' ')

if len(w1)>len(w2):
    print(w1, len(w1), sep=' ')
elif len(w1)==len(w2):
    print("same")
else:
    print(w2, len(w2), sep=' ')