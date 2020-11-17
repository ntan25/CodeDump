def sleep_in(weekday, vacation):
    if weekday == True: 
        if vacation == False: 
            return False
        else: 
            return True

    else: 
        if vacation == False:
            return True
        else: 
            return True



def diff21(n): 
    if n <= 21:
        a = 21 - n
        if a < 0: 
            return (-1* a)
        else: 
            return a
    else: 
        return 2*(n-21)

def parrot_trouble(talking, hour):
    if talking: 
        if hour<7 or hour>20: 
            return True
            
        else: 
            return False
            
    return False

def makes10(a, b):
    if a == 10: 
        return True
    elif b == 10: 
        return True
    else: 
        if a+b == 10: 
            return True
        else: 
            return False 

def near_hundred(n):
    return 190 <= n <= 210 or 90 <= n <= 110