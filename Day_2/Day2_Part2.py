
def totalScore(text):

    valueSelected = {'X': 1, 'Y': 2, 'Z': 3}

    shapeSelected = {'AX': 'Z', 'AY': 'X', 'AZ': 'Y',
                     'BX': 'X', 'BY': 'Y', 'BZ': 'Z',
                     'CX': 'Y', 'CY': 'Z', 'CZ': 'X'}

    outcomeRound = {'X': 0, 'Y': 3, 'Z': 6}

    with open(text, 'r') as file:
        sum = 0
        for lines in file:
            letters = lines.replace('\n', '').split(' ')
            shape = shapeSelected[letters[0] + letters[1]]
            sum += valueSelected[shape] + outcomeRound[letters[1]]

    return sum


if '__main__' == __name__:
    print(totalScore('Day2.txt'))
