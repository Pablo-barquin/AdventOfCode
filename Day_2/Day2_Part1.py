
def totalScore(text):

    shapeSelected = {'X': 1, 'Y': 2, 'Z': 3}
    outcomeRound = {'AX': 3, 'AY': 6, 'AZ': 0, 
                    'BX': 0, 'BY': 3, 'BZ': 6, 
                    'CX': 6, 'CY': 0, 'CZ': 3}
    
    with open(text, 'r') as file:
        sum = 0
        for lines in file:
            letters = lines.replace('\n', '').split(' ')
            sum += shapeSelected[letters[1]] + outcomeRound[letters[0]+letters[1]]

    return sum


if '__main__' == __name__:
    print(totalScore('Day2.txt'))