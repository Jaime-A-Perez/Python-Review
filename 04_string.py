
quote1 = "I'm Nicolas"
quote2 = 'She said "Hello!"'

#format
name = input("What´s your name?")
last_name = input("What´s your last name?")

template1 = "Hello, my name is " + name + " and my last name is " + last_name

template2 = "Hello, my name is {} and my last name is {}".format(name, last_name)

template3 = f"Hello, my name is {name} and my last name is {last_name}"

print(template1)
print(template2)
print(template3)