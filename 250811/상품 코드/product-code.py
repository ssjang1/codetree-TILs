product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.

class product:
    def __init__(self, product_name, product_code):
        self.name=product_name
        self.code=product_code

pro1 = product("codetree", 50)
pro2 = product(product_name, product_code)

print(f'product {pro1.code} is {pro1.name}')
print(f'product {pro2.code} is {pro2.name}')