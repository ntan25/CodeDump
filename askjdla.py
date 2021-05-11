cream = 'Y'
print(cream)
cream = cream.lower()
print(cream)

acceptableCream = ['y', 'n']

if cream not in acceptableCream:
    cream = 'n'
print(cream)
if cream == 'y':
    cream = 'with cream.'
print(cream)

