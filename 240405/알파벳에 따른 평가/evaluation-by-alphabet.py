word = input().upper()

if word == 'S':
    result = 'Superior'
elif word == 'A':
    result = 'Excellent'
elif word =='B':
    result = 'Good'
elif word =='C':
    result = 'Usually'
elif word =='D':
    result = 'Effort'
else:
    result = 'Failure'

print(result)