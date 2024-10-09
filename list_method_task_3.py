
#append
subjects= ["english","hindi","marathi"]
subjects.append("sanskrit")
print(subjects)
print ()

#extend
fruits= ["apple","orange"]
fruits.extend(["cherry","banana","mango"])
print(fruits)
print()

#insert
vegetables= ["brinjal","tomato","cabbage"]
vegetables.insert(2,"potato")
print(vegetables)
print()

#remove
Name=["ashu","tashu","rashi","tashi"]
Name.remove("ashu")
print(Name)
print()

#pop
colors=["red","black","orange","white","blue"]
popped_item=colors.pop()
print(colors)
print(popped_item)
print()

#clear
Name=["ashu","tashu","rashi","tashi"]
Name.clear()
print(Name)
print()

#index
subjects= ["english","hindi","marathi","science","EVS","history","geography"]
index=subjects.index("EVS")
print(index)
print ()

#count
Name=["ashu","tashu","rashi","tashu","sonu","monu","tashu"]
count=Name.count("tashu")
print(count)
print()

#sort
colors=["red","black","orange","white","blue"]
colors.sort()
print(colors)
print()

#copy
fruits= ["apple","orange"]
fruits=fruits.copy()
print(fruits)
print()