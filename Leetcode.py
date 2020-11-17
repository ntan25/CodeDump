

# def subtractProductAndSum(n): 
#     multiplier = 1
#     add = 0
#     for val in str(n): 
#         val = int(val)
#         multiplier *= val
#         add += val
        
#     return (multiplier - add)

# print(subtractProductAndSum(234))


import random 

def getNoZeroIntegers(n): 
    nums = []

    a = random.randint(0, n - 1)
    nums.append(a)
    nums.append(n - a)

    return nums


print(getNoZeroIntegers(34))


def climbStairs(n): 
    counter = 0 
    counter += 1
    

       