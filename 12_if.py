# verify par or inpar

number = int(input('Write the integer '))
#
#if int(number) :
#    print("The characters that you typed aren't integer ")
#else :
#    print("o")

if number % 2 == 0 :
    print('     The number is par')
elif number % 2 != 0 :
    print('     The number is inpar')