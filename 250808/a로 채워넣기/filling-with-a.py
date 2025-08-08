word = input()
l = len(word)
new_word = word[0]+'a'+word[2:l-2]+'a'+word[-1]

print(new_word)