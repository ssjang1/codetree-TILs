m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

num_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

s1 , s2 = 0, 0

for i in range(m1-1):
    s1 += num_of_days[i]
s1 += d1

for i in range(m2-1):
    s2 += num_of_days[i]
s2 += d2

print(s2-s1+1)