import numpy as np


def calcSand(matrix):
    tempX, tempY = np.where(matrix == '+')

    it = 0
    flag = True
    lastPoint = list()
    lastPoint.append((tempX, tempY))
    while flag:
        if tempX + 1 == matrix.shape[0]:
            flag = False
        else:
            if matrix[tempX+1, tempY] == '.':
                tempX = tempX+1
                lastPoint.append((tempX, tempY))
            elif tempY-1 > 0 and matrix[tempX+1, tempY-1] == '.':
                tempX, tempY = tempX+1, tempY-1
                lastPoint.append((tempX, tempY))
            elif tempY+1 != matrix.shape[1] and matrix[tempX+1, tempY+1] == '.':
                tempX, tempY = tempX+1, tempY+1
                lastPoint.append((tempX, tempY))
            elif tempY-1 == -1 or tempY+1 == matrix.shape[1]:
                flag = False
            else:
                matrix[tempX, tempY] = 'o'
                it += 1
                lastPoint.pop()
                if not len(lastPoint):
                    break
                tempX, tempY = lastPoint[-1][0], lastPoint[-1][1]

    return it


def obtainMatrix(data):
    maxX = max(max(d['x']) for d in data.values()) + 2
    maxY = max(max(d['y']) for d in data.values())

    matrix = np.full((maxX+1, maxY*2), '.')
    matrix[0, 500] = '+'

    for key in data.values():
        pos = list(zip(key['x'], key['y']))
        while len(pos) > 1:
            row = list(range(min(pos[0][0], pos[1][0]),
                             max(pos[0][0], pos[1][0])+1))
            col = list(range(min(pos[0][1], pos[1][1]),
                             max(pos[0][1], pos[1][1])+1))
            matrix[row, col] = '#'
            pos.pop(0)

    col = list(range(0, maxY*2))
    matrix[maxX, col] = '#'

    return matrix


def unitsOfSand(text):

    with open(text, 'r') as file:
        data = [x.strip().split(' -> ') for x in file.readlines()]

        draw = dict()
        for pos, line in enumerate(data):
            x, y = [], []
            for aux in line:
                tempY, tempX = aux.split(',')
                x.append(int(tempX)), y.append(int(tempY))
            draw[pos] = {'x': x, 'y': y}

        matrix = obtainMatrix(draw)

        return calcSand(matrix)


if '__main__' == __name__:
    print(unitsOfSand('Day14.txt'))
