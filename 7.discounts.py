# 7) Calculate Discounts for Products
#  You have a list of products with their prices. 
# Apply a 20% discount to products costing more than $100 and return the updated prices.

# 	products = [
#     {"name": "Laptop", "price": 1200},
#     {"name": "Headphones", "price": 80},
#     {"name": "Smartphone", "price": 700},
#     {"name": "Monitor", "price": 150}
#    ]

# list out discounted products

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Headphones", "price": 80},
    {"name": "Smartphone", "price": 700},
    {"name": "Monitor", "price": 150}
   ]
p=filter(lambda x:x['price']>100,products)
pi=list(p)
print(list(pi))
g=map(lambda x:x['name'] x["price"]*0.8,pi)
print (list(g))