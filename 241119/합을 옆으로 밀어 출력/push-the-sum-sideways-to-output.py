n = int(input())
tot =0
for i in range(n):
    line = int(input())
    tot += line

word = str(tot)

print(word[1:]+word[0])