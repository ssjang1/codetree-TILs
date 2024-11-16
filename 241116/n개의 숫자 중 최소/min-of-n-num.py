a = list(map(int,input().strip().split(' ')))

min_v = a[0]

for e in a[1:]:
    if min_v > e:
        min_v = e

print(min_v, a.count(min_v), end=" ")