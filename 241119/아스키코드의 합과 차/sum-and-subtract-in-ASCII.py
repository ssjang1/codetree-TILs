char1, char2 = input().split(' ')

hap = ord(char1)+ord(char2)

value = ord(char1)-ord(char2)
cha = value if value>=0 else -value

print(hap, cha, end=' ')
