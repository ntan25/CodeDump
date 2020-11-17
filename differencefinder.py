# identify the first instance of a difference in base pairs
# file1 = open('/Users/neeltangella/Desktop/DNA.txt', 'r')
# file2 = open('/Users/neeltangella/Desktop/DNA copy.txt', 'r')
list_1 = file1.read()
list_2 = file2.read()


def difference(dnastring_1, dnastring_2):
    for i in range(0, len(dnastring_1)):
        lister1 = list(dnastring_1)
        lister2 = list(dnastring_2)
        if lister1[i] == lister2[i]:
            continue
        else:
            return i

print(difference(list_1, list_2))