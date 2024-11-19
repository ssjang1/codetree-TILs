word, q = input().split(' ')

q = int(q)

for i in range(q):
    line = int(input())
    if line ==1:
        word = word[1:]+word[0]
    elif line ==2:
        word = word[-1] + word[:-1]
    else:
        word = word[-1::-1]
    print(word)