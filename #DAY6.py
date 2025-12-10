#DAY6

a = 1
b = "sing"
c = True
d = None
print("this is a ", type(a), "type")
print("this is a ", type(b), "type")
print("this is a ", type(c), "type")
print("this is a ", type(d), "type")
#type function is used to find the type of variable
e = complex(2, 3)
print(e)
#complex function is used to create complex number
list = [1, 2, 3, 4, 5, 'apple , banana, cherry']
print(list)
#list is a collection of the items which is ordered and changeable and allow duplicate values
tuple = (("banana","apple"), ("Cherry","oranges"))
print(tuple)
#tuple is a collection of the item which is ordered and unchangeable and allow duplicate values and its immutable
dict = {"Name":"Ayan","age" :20,"CanVote":"Yes"}
print(dict)
#dictionary is a collection of the item which is unordered and changeable and do not allow duplicate values and its mutable and it is written in key value pair 

'''
Note
'''
# In Python, the primary difference between a key-value store (like a dictionary) and an object (like instances of classes) can be summarized as follows:
# Key-Value Store
# Structure: A key-value store is essentially a collection of key-value pairs where each key is unique. In Python, this can be represented using dictionaries.
# Access: Data is accessed via keys. For example:
# my_dict = {"name": "Ayan", "age": 20}
# print(my_dict["name"])  # Outputs: Ayan
# Mutability: Keys must be immutable (strings, numbers, or tuples), while values can be of any data type.
# Use: Ideal for storing related data that can be accessed via unique identifiers.
