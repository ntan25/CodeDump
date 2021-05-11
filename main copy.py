#Neel Tangella 
#ITP 115, Spring 2021
#Assignment 3 


selection = input('Please select an item from the vending machine: \n \ta) Butterbeer: 58 knuts \n '
' \tb) Quill: 10 knuts \n \tc) The Daily Prophet: 7 knuts \n \td) Book of Spells: 400 knuts \n'
'>')

willShare = 'Will you share this on Instagram (y/n)?'

willShare.casefold()
selection.casefold()

acceptableselection = ['a', 'b', 'c', 'd']
acceptableShare = ['y', 'n']

if selection not in acceptableselection:
    print('You have entered an invalid option. You will be given a Butterbeer for 58 knuts.')
    selection = 'b'

if willShare not in acceptableShare:
    print("You have entered an invalid option. No coupon wil be used.")
    willShare = 'n'

    
def coupon(will_share):
    discount = 0
    if will_share == 'y':
        print("Thanks! You get 5 knuts off your purchase.")
        discount = 5
    return discount

discount = coupon(willShare)


def itemSelector(selection): 
    cost = 0 
    item = ''
    if selection == 'a':
        cost = 58 
        item = 'Butterbeer'
    elif selection == 'b':
         cost = 10 
         item = 'Quill'
    elif selection == 'c': 
        cost = 7 
        item = 'The Daily Prophet'
    else:
        cost = 400 
        item = 'Book of Spells'
    return cost, item 

cost, item = itemSelector(selection)

