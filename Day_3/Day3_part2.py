import numpy as np


def sumOfPrioritiesGroups(text):

    badge = []
    with open(text, 'r') as file:
        elvesRucksack = [x.replace('\n', '') for x in file.readlines()]
        allGroups = np.array_split(elvesRucksack, len(elvesRucksack)/3)

        for array in allGroups:
            badge += list(set(array[0]) & set(array[1]) & set(array[2]))

        sumValue = [ord(x)-96 if x.islower() else ord(x)-38 for x in badge]

        return sum(sumValue)


if '__main__' == __name__:
    print(sumOfPrioritiesGroups('Day_3/Day3.txt'))
