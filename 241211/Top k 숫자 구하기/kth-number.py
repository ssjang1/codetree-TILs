n,k = map(int,input().strip().split(' '))

numbers = list(map(int,input().strip().split(' ')))
numbers.sort()

print(numbers[k-1])