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

print(sequencegenerator(random_sequence, 10))
