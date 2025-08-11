unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.

class answer:
    def __init__(self, unlock_code, wire_color, seconds):
        self.code = unlock_code
        self.color = wire_color
        self.second = seconds

a = answer(unlock_code, wire_color, seconds)

print(f'code : {a.code}')
print(f'color : {a.color}')
print(f'second : {a.second}')