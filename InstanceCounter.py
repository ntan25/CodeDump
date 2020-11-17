import random

random_sequence = []


def sequencegenerator(empty_list, desired_bases):
    for i in range(0, desired_bases):
        a = (random.randint(1, 4))
        if a == 1:
            empty_list.append('A')
        elif a == 2:
            empty_list.append('G')
        elif a == 3:
            empty_list.append('T')
        else:
            empty_list.append('C')
    return empty_list

aa = sequencegenerator(random_sequence, 10000000)



def InstanceCounter(DNA, instance): 
    

    for i in range(0, len(DNA), len(instance)):
        counter = 0
        location = []
        if DNA[i: i+len(instance)] == instance: 
            counter += 1
            a = "{}-{}".format(i, i + len(instance))
            location.append(a)

        
    return counter, location
# print(aa)
print(InstanceCounter(random_sequence, ['A', 'G', 'C']))

