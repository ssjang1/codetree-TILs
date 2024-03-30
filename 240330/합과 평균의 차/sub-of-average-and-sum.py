a,b,c = map(int, input().split(' '))

print(sum([a,b,c]))
print(int(sum([a,b,c])/3))
print(int(sum([a,b,c])-sum([a,b,c])/3))