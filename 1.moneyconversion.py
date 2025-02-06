# 1) convert the prices in USD & Euro using appropriate function
#     PricesList_inr =[3000,56000,45000,2300]

currency=[3000,56000,45000,2300]
changed_euro=map(lambda x:x/90,currency)
changed_dollar=map(lambda x:x/86,currency)
print(list(changed_dollar))
print(list(changed_euro))





