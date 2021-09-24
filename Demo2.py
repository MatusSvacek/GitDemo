values = [1, 2, 3, "hello", 4]

# List is a data type that allows multiple values and can be different data types

print(values[0]) # 1
print(values[3]) # hello
print(values[-1]) # 4
print(values[1:3]) #2 3
values.insert(4, "world") #add world to 4th index
print(values)
values.append("end")
print(values)

values[2] = "RAHUL" #updates value at 2nd index
del values[0] #deletes value at 1st index
print(values)

#Tuple - same as list data type but cant be updated changed
val = (1, 2, "hello", 4, 5)
print(val[1])

# Dictionary
dic = {"a":2, 4:"bcd", "c":"hello world"}
print(dic["c"])

#
dict = {}
dict["firstname"] = "Matus"
dict["lastname"] = "Svacek"
dict["gender"] = "Male"

print(dict)
print(dict["firstname"])