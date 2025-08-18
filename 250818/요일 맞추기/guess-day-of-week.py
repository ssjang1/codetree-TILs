m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

month_days = [31,28,31,30,31,30,31,31,30,31,30,31]

def how_many_days(m, d):
    days = 0

    for i in range(m-1):
        days += month_days[i]
    days += d

    return days

s1 = how_many_days(m1, d1)
s2 = how_many_days(m2, d2)

diff_days = s2- s1

diff_7 = diff_days % 7

day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print(day_of_week[diff_7])