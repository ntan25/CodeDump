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


def missing_char(str, n):
    a = str[n]
    return str.replace(a, '')



def monkey_trouble(a_smile, b_smile):
    if a_smile: 
        if b_smile: 
            return True
        else: 
            return False
    else: 
        if b_smile: 
            return False
        else: 
            return True

def sum_double(a, b):
    if a == b: 
        return 4*a
    else: 
        return a + b

def string_times(str, n):
    return n*str

def front_times(str, n):
    a = str[0:3]
    return n*a

def string_bits(str):
    a = ''
    for i in range(0, len(str)- 1, 2):
        aa = str[i]
        a += aa
        
    return a


def twoSum(self, nums, target):

        aa = []

        for i in nums:



            for j in nums:

                if nums[i] + nums[j] == target:
                    aa.append(i,j)
                    break

        return aa
        
