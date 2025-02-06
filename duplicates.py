# write a program to remove the duplicates in the list
#  numbers3=[2,2,4,6,3,4,6,1]
numbers=[2,2,4,6,3,4,6,1]
res=[]
for i in numbers:
    if i in res:
        continue
    else:
        res.append(i)
print(res)

