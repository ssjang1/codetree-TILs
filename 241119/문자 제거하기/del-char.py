word = input()

while len(word) >=2:
    num = int(input())
    if num >= len(word):
        word = word[:-1]
    else:
        word = word[:num] + word[num+1:]
    print(word)