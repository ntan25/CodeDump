#Neel Tangella, tangella@usc.edu
#ITP 115, Spring 2021
#Lab 2

#taking in user input
size = input("What size coffee do you want(S, M, L)?")
temp = int(input("What temperature would you like (in degrees)?"))
bean = input("What type of beans/blend would you like?")
cream = input("Would you like room for cream?")

#making sure that all the input is in one case so that the functions need to account for less cases
size.lower()
cream.lower()
print(cream)
#creating acceptable values so that the program knows how to deal with other values
acceptableSize = ['s', 'm', 'l']
acceptableCream = ['y', 'n']

#if response is not acceptable, assigning values to the variables
if size not in acceptableSize:
    size = 'm'

if cream not in acceptableCream:
    cream = 'n'
print(cream)
# series of if/else statements to determine outputs
breakingPoint = 90
if temp <= breakingPoint:
    temp = 'iced'
else:
    temp = 'hot'

if cream == 'y':
    cream = 'with cream.'
else:
    cream = 'with no cream.'

if size == 's':
    size = 'small'
elif size == 'm':
    size = 'medium'
else:
    size = 'large'


# stripping whitespace
temp = temp.strip()
cream = cream.strip()
size = size.strip()
bean = bean.strip ()
print(cream)
#printing the final summary statement
# print('You ordered a {asize} {atemp} {abean} coffee {acream}'.format(asize = size, atemp = temp, abean = bean,
# acream = cream))
