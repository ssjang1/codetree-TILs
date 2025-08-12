n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.

class Day:
    def __init__(self,date,day,weather):
        self.date=date
        self.day=day
        self.weather=weather

days = [Day(d,dy,w) for d,dy,w in zip(date,day,weather)]

idx = 0

next_rain ='9999-12-31'

for i, (d,dy,w) in enumerate(zip(date,day,weather)):
    if w == 'Rain':
        if next_rain > d:
            next_rain = d
            idx = i

print(days[idx].date, days[idx].day, days[idx].weather, end=' ')
