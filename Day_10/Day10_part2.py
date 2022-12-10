import numpy as np


def saveValue(cycle, crt, register):
    row = cycle//40
    col = cycle % 40

    if col in register:
        crt[row, col] = '#'
    else:
        crt[row, col] = '.'


def printCRT(data, crt):
    cycle = 0
    registerX = [0, 1, 2]
    while cycle < 240:
        line = data[0].split(' ')
        if line[0] == 'noop':
            saveValue(cycle, crt, registerX)
            cycle += 1
        else:
            cycleTemp = cycle
            while cycle < cycleTemp+2:
                saveValue(cycle, crt, registerX)
                cycle += 1
            registerX = [x+int(line[-1]) for x in registerX]
        data.pop(0)


def spriteCRT(text):

    with open(text, 'r') as file:
        data = [x.strip() for x in file.readlines()]
        crt = np.full((6, 40), '#')
        printCRT(data, crt)

        file.close()

    for row in crt:
        for col in row:
            print(col, end='')
        print()


if '__main__' == __name__:
    spriteCRT('Day_10/Day10.txt')
