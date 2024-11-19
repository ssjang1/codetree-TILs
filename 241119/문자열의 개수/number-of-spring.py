words = []
while True:
    line = input()
    if line =='0':
        break
    words.append(line)

print(len(words))
hol = words[0::2]
for i in range(len(hol)):
    print(hol[i])