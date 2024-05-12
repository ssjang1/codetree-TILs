total = []
while True:
    n= int(input())
    if 20<= n <30:
        total.append(n)
    else:
        result = round(sum(total)/len(total),2)
        print(f"{result:.2f}")
        break