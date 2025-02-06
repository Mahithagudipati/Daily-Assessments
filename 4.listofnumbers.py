# # 4) You have a list of numbers. Filter out the odd ones, 
# # double the even numbers, and sort them in ascending order

numbers=[12,22,14,18,16,27,23]
odd=filter(lambda x :(x%2!=0),numbers)
o=list(odd)
even=filter(lambda x :(x%2==0),numbers)
evenlist=map(lambda x :x*2,even)
e=list(evenlist)
o.extend(e)
o.sort()
print(list(o))
# evenn=list(evenlist)
# print(list(evenn))
# # sorted_result=sorted(evenlist,key=lambda x:x)
# # print(list(sorted_result))
# evenn.sort()
# print(list(evenn))
