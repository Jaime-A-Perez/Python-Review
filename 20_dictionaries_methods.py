person = {
    'name'      : 'Nico',
    'last_name' : 'Molina',
    'langs'     : ['python, javascript'],
    'age'       : 59
}

print(f"person {person}")


person['name'] = 'Santi'
person['age'] += 2
person['langs'].append('rust')

print(f"person modified{person}")


del person['last_name']
person.pop('age')

print(f"person with deleted methods {person}")


print(f"items()   = {person.items()}")

print(f"keys()    = {person.keys()}")
list_keys = list(person.keys())
print(f"types(keys())    = {type(list_keys)}")

print(f"values()  = {person.values()}")
