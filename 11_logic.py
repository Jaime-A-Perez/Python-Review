# and

print("     and")

print('True and True =>', True and True) 
print('True and False =>', True and False) 
print('False and True =>', False and True) 
print('True and False =>', False and False) 

print("10 > 5 and 5 > 10", 10 > 5 and 5 > 10)
print("10 > 5 and 5 < 10", 10 > 5 and 5 < 10)

stock_range = input('Write the cuantity of products => ')
stock_range = int(stock_range)
print(stock_range  >= 100 and stock_range <= 1000)


print("     or")

print('True or True =>', True or True) 
print('True or False =>', True or False) 
print('False or True =>', False or True) 
print('True or False =>', False or False) 

print("10 > 5 or 5 > 10", 10 > 5 or 5 > 10)
print("10 > 5 or 5 < 10", 10 > 5 or 5 < 10)

role = input('Write your role => ')
print(role == 'admin' or role == 'seller')


print("     not")

print(' not True or True =>', not (True or True)) 
print(' not True or False =>', not (True or False)) 
print(' not False or True =>', not (False or True)) 
print(' not True or False =>', not (False or False)) 

print("10 > 5 or 5 > 10", 10 > 5 or 5 > 10)
print("10 > 5 or 5 < 10", 10 > 5 or 5 < 10)

role = input('Write your role => ')
print(not (role == 'admin' or role == 'seller'))