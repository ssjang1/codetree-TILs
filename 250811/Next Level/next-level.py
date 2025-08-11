user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.

class user:
    def __init__(self, id, level):
        self.id = id
        self.level = level

u1 = user("codetree",10)
u2 = user(user2_id, user2_level)

print(f'user {u1.id} lv {u1.level}')
print(f'user {u2.id} lv {u2.level}')