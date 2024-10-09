
#change
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2018
print(car)

#update
employee = {
  "emp_id": "abcdefg",
  "designation": "manager",
  "salary": 15000
}
employee.update({"salary": 25000})
print(employee)

#adding items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#pop
my_dict = {"name":"akansha","age":20,"gender":"female"}
gender = my_dict.pop("gender")
print(gender)
print(my_dict)

#set default
default = {"name":"ashu","city":"nagpur"}
state =default.setdefault("state","maharasthra")
print(state)
print(default) 

#clear
my_dict = {"name":"akansha","age":20,"gender":"female"}
my_dict.clear()
print(my_dict)

#fromkeys
keys = ["name","age","salary","city","state"]
my_dict = dict.fromkeys(keys, "unknown")
print(my_dict)

