m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.

month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def how_many_days(m, d):
    days = 0
    for i in range(m-1):
        days += month_days[i]
    days += d

    return days

day1 = how_many_days(m1, d1)
day2 = how_many_days(m2, d2)

g_d = day2 - day1

# print(day_of_week.index(A))
# if g_d % 7 >= day_of_week.index(A) + 1:
#     print(g_d//7 + 1)
# else:
#     print(g_d//7)

cnt = 0
for i in range(day1, day2+1):
    if i % 7 == day_of_week.index(A):
        cnt += 1

print(cnt)