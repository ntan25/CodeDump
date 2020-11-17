list = "AGCAGCAGCAGCAGC"

def instance_count(list, DNA_String):
    aa = []
    for char in list:
        aa.append(char)
    count = 0
    for chars in range(0, len(aa)- 1, len(DNA_String)):
        if chars == DNA_String:
            count += 1

    return count

print(instance_count(list, "AGC"))