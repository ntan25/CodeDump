import time
start_time = time.time()

file = open('/Users/neeltangella/Desktop/DNA.txt', 'r') #only takes text files
original = file.read()
proper = []

for char in original:
    proper.append(char)

# print("original sequence= {}".format(proper))
complement = []
for base in proper:
    if base == 'A':
        complement.append('T')
    elif base == 'G':
        complement.append('C')
    elif base == 'C':
        complement.append('G')
    else:
        complement.append('A')

# print("complement sequence= {}".format(complement))
rna = []
for val in proper:
    if val == 'A':
        rna.append('U')
    elif val == 'G':
        rna.append('C')
    elif val == 'C':
        rna.append('G')
    else:
        rna.append('A')

# print("RNA sequence= {}".format(rna))
triples = []
for i in range(0, len(rna), 3):
    a = complement[i:i + 3]
    triples.append(a)


def convert(list):
    return tuple(list)

newtrip = convert(triples)

dictionary_DNA = {('A', 'T', 'A'):'I', ('A', 'T', 'C'):'I', ('A', 'T', 'T'):'I', ('A', 'T', 'G'):'M',
        ('A', 'C', 'A'):'T', ('A', 'C', 'C'):'T', ('A', 'C', 'G'):'T', ('A', 'C', 'T'):'T',
        ('A', 'A', 'C'):'N', ('A', 'A', 'T'):'N', ('A', 'A', 'A'):'K', ('A', 'A', 'G'):'K',
        ('A', 'G', 'C'):'S', ('A', 'G', 'T'):'S', ('A', 'G', 'A'):'R', ('A', 'G', 'G'):'R',
        ('C', 'T', 'A'):'L', ('C', 'T', 'C'):'L', ('C', 'T', 'G'):'L', ('C', 'T', 'T'):'L',
        ('C', 'C', 'A'):'P', ('C', 'C', 'C'):'P', ('C', 'C', 'G'):'P', ('C', 'C', 'T'):'P',
        ('C', 'A', 'C'):'H', ('C', 'A', 'T'):'H', ('C', 'A', 'A'):'Q', ('C', 'A', 'G'):'Q',
        ('C', 'G', 'A'):'R', ('C', 'G', 'C'):'R', ('C', 'G', 'G'):'R', ('C', 'G', 'T'):'R',
        ('G', 'T', 'A'):'V', ('G', 'T', 'C'):'V', ('G', 'T', 'G'):'V', ('G', 'T', 'T'):'V',
        ('G', 'C', 'A'):'A', ('G', 'C', 'C'):'A', ('G', 'C', 'G'):'A',('G', 'C', 'T'):'A',
        ('G', 'A', 'C'):'D', ('G', 'A', 'T'):'D', ('G', 'A', 'A'):'E', ('G', 'A', 'G'):'E',
        ('G', 'G', 'A'):'G', ('G', 'G', 'C'):'G', ('G', 'G', 'G'):'G', ('G', 'G', 'T'):'G',
        ('T', 'C', 'A'):'S', ('T', 'C', 'C'):'S', ('T', 'C', 'G'):'S', ('T', 'C', 'T'):'S',
        ('T', 'T', 'C'):'F', ('T', 'T', 'T'):'F', ('T', 'T', 'A'):'L', ('T', 'T', 'G'):'L',
        ('T', 'A', 'C'):'Y', ('T', 'A', 'T'):'Y', ('T', 'A', 'A'):'_', ('T', 'A', 'G'):'_',
        ('T', 'G', 'C'):'C', ('T', 'G', 'T'):'C', ('T', 'G', 'A'):'_', ('T', 'G', 'G'):'W', }
finalist = []
for a in newtrip:
    b = convert(a)
    finalist.append(b)
# print(finalist)
amino = []

for a in finalist:
    appendage = dictionary_DNA.get(a)
    amino.append(appendage)

print("amino acid sequence= {}".format(amino))
runtime = (time.time()- start_time)
print("{} base pairs sequenced in {} seconds".format(len(proper),runtime))