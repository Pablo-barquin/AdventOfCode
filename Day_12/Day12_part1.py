import numpy as np


def get_neighbours(matrix, pos, closed):

    queue = list()

    for x2, y2 in ((pos[0]+1, pos[1]), (pos[0]-1, pos[1]), (pos[0], pos[1]+1), (pos[0], pos[1]-1)):
        if 0 <= x2 < matrix.shape[0] and 0 <= y2 < matrix.shape[0] and (x2, y2) not in closed:
            if matrix[x2, y2] == 69:
                number1, number2 = matrix[pos[0], pos[1]], ord('z')
            else:
                number1, number2 = matrix[pos[0], pos[1]], matrix[x2, y2]
            if number1 + 1>= number2:
                queue.append((x2, y2))

    return queue



def best_first_search(matrix):

    i, j = np.where(matrix == 83)
    matrix[i, j] = ord('a')

    closed = set()
    open = [(int(i), int(j))]

    flag = False
    it = 0
    while open and flag == False:
        pos = open.pop(0)
        closed.add((pos[0], pos[1]))
        if matrix[pos[0], pos[1]] == 69:
            flag = True
        else:
            open = get_neighbours(matrix, pos, closed) + open
        it += 1

    return it


def fewestSteps(text):

    with open(text, 'r') as file:
        data = [[*x.strip()] for x in file.readlines()]
        for i, line in enumerate(data):
            data[i] = [ord(x) for x in line]
        matrix = np.array(data)

        return best_first_search(matrix)


if '__main__' == __name__:
    print(fewestSteps('Day_12/Day12.txt'))
