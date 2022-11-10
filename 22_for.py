for element in range(4):
    print(element)

for i in range(3, 9):
    print(i)

my_list = [22, 33, 44, 55, 66]
for n in my_list:
    print(n)

my_tuple = ("p", "r", "d", "4")
for l in my_tuple:
    print(l)

my_product = {
    'name'  :   'Nico',
    'age'   :   34
}    
for key in my_product:
    print(key)
for key, value in my_product.items():
    print(key, '=', value )


people = [
    {
        'name'  :   "Ana",
        'age'   :   2
    },
    {
        'name'  :   'Carl',
        'age'   :   1
    }
]

for person in people:
    print(person)

for person in people:
    print(person['name'])