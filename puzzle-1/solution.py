inp = [line.strip() for line in open('input.txt')]
totCals = []

def p1():
    for elf in ('\n'.join(inp)).split('\n\n'):
        cals=0
        for x in elf.split('\n'):
            cals += int(x)
        totCals.append(cals)
    return (max(totCals))

def p2():
    sortedCals = sorted(totCals)
    size = len(sortedCals)
    result = sortedCals[size-1] + sortedCals[size-2] + sortedCals[size-3]
    return result

print(p1())
print(p2())