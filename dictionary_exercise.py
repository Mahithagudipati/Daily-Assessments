# Exercise on Dictionary
# ----------------------

# 1)  calculate count the item frequency from the below products and store it in dictionary
# products="yogurt eggs cookies cookies eggs yogurt apple yogurt apple"

# 2) Store management
   
#   initial_stock = {"apple": 50,"banana": 100,"orange": 75}

#   sold_item = {"apple": 10, "banana": 20, "orange": 15}

#   calculate the current stock and display current stock

# 3)You have sales data for different regions and want to calculate the total sales for each region.

#     sales_data = [
#     {"region": "North", "sales": 15000},
#     {"region": "South", "sales": 8000},
#     {"region": "West", "sales": 7000},
#     {"region": "East", "sales": 5000},
#     {"region": "South", "sales": 12000}
#     {"region": "West", "sales": 7000},
#     {"region": "East", "sales": 5000},
#     {"region": "South", "sales": 12000}
# ]

# 4) take input of your mobile number and display it in word format

#  234= two three four
#----------------------------------------------------------------------------------------------------
def prod(s):
    store={}
    for i in s:
        if i in store:
            store[i]+=1
        else:
            store[i]=1
    return store

def main():
    s= ['yogurt', 'eggs','cookies', 'cookies', 'eggs', 'yogurt', 'apple', 'yogurt', 'apple']
    print(prod(s))
main()
#---------------------------------------------------------------------------------------------------------

initial_stock = {"apple": 50,"banana": 100,"orange": 75}
sold_item = {"apple": 10, "banana": 20, "orange": 15}
#   calculate the current stock and display current stock
result_dict = {key: initial_stock[key] - sold_item[key] for key in initial_stock if key in sold_item}
print(result_dict)
#-------------------------------------------------------------------------------------------------------

phone_number={1:' one ',2:' two ',3:' three ',4:' four ',5:' five ',6:' six ',7:' seven ',8:' eight ',9:' nine ',0:' zero '}
n=input("Enter the phone number : ")
for i in n:
    print(phone_number.get(int(i)),end="")

