word, char = input().split(' ')

if char in word:
    print(word.index(char))
else:
    print("No")