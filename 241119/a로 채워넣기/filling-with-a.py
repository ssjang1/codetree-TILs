line1 = input()

a = list(line1)

a[1] ='a'
a[-2] ='a'

answer = ''.join(a)
print(answer)