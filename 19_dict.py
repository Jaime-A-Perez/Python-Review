my_dict = {}
print(type(my_dict))

my_dict = {
    "name"      :   "Nicolas",
    "last_name" :   "Molina",
    "age"       :   73
}

print(f"my_dict  {my_dict}")
print(f"len(my_dict) {len(my_dict)}")

print(f"my_dict['age'] {my_dict['age']}")
print(f"my_dict['another'] {my_dict.get('another')}")