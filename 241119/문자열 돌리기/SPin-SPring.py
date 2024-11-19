word = input()

length = len(word)

print(word)
for i in range(length):
    word = word[-1]+word[:-1]
    print(word)