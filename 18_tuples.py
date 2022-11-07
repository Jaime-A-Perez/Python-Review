# Important: Tuples are inmutables
numbers_tuple = (1,2,3,5,6)
strings_tuple = ("Hello","world")
print(f"numbers_tuple {numbers_tuple}")
print (f"type(numbers_tuple {type(numbers_tuple)}")

print(f"numbers_tuple[2] = {numbers_tuple[2]}")

print(f"numbers_tuple.index(3) = {numbers_tuple.index(3)}")


# tuple to list

numbers_list = list(numbers_tuple)
print(f"numbers_list {numbers_list}")
print(f"type(numbers_list {type(numbers_list)})")