n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Please write your code here.
class person:
    def __init__(self, name, street_address, region):
        self.name =name
        self.street_address = street_address
        self.region = region

people = []
for na, add, re in zip(name, street_address, region):
    people.append(person(na,add,re))

people.sort(key= lambda person:person.name, reverse=True)

print(f'name {people[0].name}')
print(f'addr {people[0].street_address}')
print(f'city {people[0].region}')