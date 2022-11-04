# CRUD: CREATE READ UPDATE DELET

numbers = [1 , 4 ,5, 6, 2]
print("numbers ", numbers)

print("last element ", numbers[-1])

print("add new element to end ", numbers.append(43))

print("insert into index a new element  ", numbers.insert(0, 23))

numbers2 = [33, 44, 66]
# Addition of arrays
numbers3 = numbers + numbers2

print("return index of element  ", numbers.index(23))

print("remove element  ", numbers.remove(23))

print("remove element at end ", numbers.pop())

print("remove element at index  ", numbers.pop(4))

print("reverse the array  ", numbers.reverse())

print("short the array  ", numbers.sort())

