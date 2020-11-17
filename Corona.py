genes = open("/Users/neeltangella/Desktop/Corona Genes.txt", "r")

aa = genes.read()

corona = []

for char in aa:
    corona.append(char)

for char in corona:
    if char not in "acgt":
        corona.remove(char)

bb = []


def grouper(list):
    for i in range(0, len(list), 3):
        bb.append(tuple(list[i:i + 3]))

    return (bb)


grouper(corona)

dictionary_DNA = {('a', 't', 'a'): 'I', ('a', 't', 'c'): 'I', ('a', 't', 't'): 'I', ('a', 't', 'g'): 'M',
                  ('a', 'c', 'a'): 'T', ('a', 'c', 'c'): 'T', ('a', 'c', 'g'): 'T', ('a', 'c', 't'): 'T',
                  ('a', 'a', 'c'): 'N', ('a', 'a', 't'): 'N', ('a', 'a', 'a'): 'K', ('a', 'a', 'g'): 'K',
                  ('a', 'g', 'c'): 'S', ('a', 'g', 't'): 'S', ('a', 'g', 'a'): 'R', ('a', 'g', 'g'): 'R',
                  ('c', 't', 'a'): 'L', ('c', 't', 'c'): 'L', ('c', 't', 'g'): 'L', ('c', 't', 't'): 'L',
                  ('c', 'c', 'a'): 'P', ('c', 'c', 'c'): 'P', ('c', 'c', 'g'): 'P', ('c', 'c', 't'): 'P',
                  ('c', 'a', 'c'): 'H', ('c', 'a', 't'): 'H', ('c', 'a', 'a'): 'Q', ('c', 'a', 'g'): 'Q',
                  ('c', 'g', 'a'): 'R', ('c', 'g', 'c'): 'R', ('c', 'g', 'g'): 'R', ('c', 'g', 't'): 'R',
                  ('g', 't', 'a'): 'V', ('g', 't', 'c'): 'V', ('g', 't', 'g'): 'V', ('g', 't', 't'): 'V',
                  ('g', 'c', 'a'): 'A', ('g', 'c', 'c'): 'A', ('g', 'c', 'g'): 'A', ('g', 'c', 't'): 'A',
                  ('g', 'a', 'c'): 'D', ('g', 'a', 't'): 'D', ('g', 'a', 'a'): 'E', ('g', 'a', 'g'): 'E',
                  ('g', 'g', 'a'): 'G', ('g', 'g', 'c'): 'G', ('g', 'g', 'g'): 'G', ('g', 'g', 't'): 'G',
                  ('t', 'c', 'a'): 'S', ('t', 'c', 'c'): 'S', ('t', 'c', 'g'): 'S', ('t', 'c', 't'): 'S',
                  ('t', 't', 'c'): 'F', ('t', 't', 't'): 'F', ('t', 't', 'a'): 'L', ('t', 't', 'g'): 'L',
                  ('t', 'a', 'c'): 'Y', ('t', 'a', 't'): 'Y', ('t', 'a', 'a'): '_', ('t', 'a', 'g'): '_',
                  ('t', 'g', 'c'): 'C', ('t', 'g', 't'): 'C', ('t', 'g', 'a'): '_', ('t', 'g', 'g'): 'W'}

answer = []

for val in bb:
    appendage = dictionary_DNA.get(val)
    answer.append(appendage)

print(answer)
