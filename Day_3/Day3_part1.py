
def sumOfPriorities(text):

    itemType = []
    with open(text, 'r') as file:
        for lines in file:
            rucksack = lines.replace('\n', '')
            itemType += list(set(rucksack[:len(rucksack)//2])
                             & set(rucksack[len(rucksack)//2:]))

        sumValue = [ord(x)-96 if x.islower() else ord(x)-38 for x in itemType]

    return sum(sumValue)


if '__main__' == __name__:
    print(sumOfPriorities('Day3.txt'))
