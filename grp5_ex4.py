my_list = ["cucumber", 42, True, "banana", 3.14]
my_tuple = ("orange", 23, False)
my_set = {"apple", 99, True}
my_dict = {
    "name": "Marry",
    "age": 39,
    "is_student": False,
}

if "apple" in my_list:
    print("The string 'cucumber' is in the list: True")
else:
    print("The string 'cucumber' is in the list: False")

if 42 in my_tuple:
    print("The integer 42 is in the tuple: True")
else:
    print("The integer 42 is in the tuple: False")

if True in my_set:
    print("The boolean True is in the set: True")
else:
    print("The boolean True is in the set: False")

if 'name' in my_dict:
    print("The key 'name' exists in the dictionary: True")
else:
    print("The key 'name' exists in the dictionary: False")

print("\nFinal Results:")
print("Check for 'cucumber' in list:", "cucumber" in my_list)
print("Check for 42 in tuple:", 42 in my_tuple)
print("Check for True in set:", True in my_set)
print("Check for 'name' in dictionary:", 'name' in my_dict)
