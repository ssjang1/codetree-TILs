def find_mini(*args):
    return min(args)

a,b,c = map(int,input().strip().split(' '))

print(find_mini(a,b,c))