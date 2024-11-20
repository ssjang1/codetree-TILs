s = input()

def check(s):
    a = set()
    for i in s:
        if i not in a:
            a.add(i)
    
    if len(a)>=2:
        return True
    else:
        return False

if check(s):
    print("Yes")
else:
    print("No")