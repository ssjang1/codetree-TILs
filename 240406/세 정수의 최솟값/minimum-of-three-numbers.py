a, b, c = map(int, input().split())

min_value = a

if b < min_value:
    min_value = b
if c < min_value:
    min_value = c

print(min_value)