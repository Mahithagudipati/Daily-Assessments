# 2) student_name_list =["Meghan","Praavalika", "Bharath","Madhu Venkata suriya Narayana","Nithin Rajesh","Mani Prasad","Samalla Akshay"]
#     List the name which has more than 6 characters as lone_names list using appropriate function

student_name_list =["Meghan","Praavalika", "Bharath","Madhu Venkata suriya Narayana","Nithin Rajesh","Mani Prasad","Samalla Akshay"]
lone_names=[]
for items in student_name_list:
    if len(items)>6:
        lone_names.append(items)
print(list(lone_names))
