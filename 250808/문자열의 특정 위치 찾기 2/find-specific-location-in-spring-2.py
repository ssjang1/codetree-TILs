words = ["apple", "banana", "grape", "blueberry", "orange"]

alphabet = input()
cnt = 0

for word in words:
    if word[2] == alphabet or word[3] == alphabet:
        print(word)
        cnt += 1

print(cnt)