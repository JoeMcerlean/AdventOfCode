inp = [line.strip() for line in open('input.txt')]

def p1():
    score = 0
    actionTwo = {'X': 1, 'Y': 2, 'Z': 3}
    for game in inp:
        me = game.rsplit(' ',1)[-1]
        score += actionTwo[me]
        if(game == 'A X' or game == 'B Y' or game == 'C Z'):
            score += 3
        if(game == 'A Y' or game == 'B Z' or game == 'C X'):
            score += 6
    return score

def p2():
    score = 0
    actions = {'A': 1, 'B': 2, 'C': 3}
    result = {'X': 0, 'Y': 3, 'Z': 6}
    for game in inp:
        elf,me = game.split()
        elfAction = actions[elf]
        score += result[me]
        if(result[me] == 6):
            score += elfAction % 3 + 1
        if(result[me] == 3):
            score += elfAction
        if(result[me] == 0):
            score += (elfAction+1) % 3 + 1 
    return score

print(p1())
print(p2())