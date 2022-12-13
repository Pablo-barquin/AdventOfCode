import numpy as np


def get_neighbours(matrix, pos, end, closed):
    queue = list()

    for x2, y2 in ((pos[0]+1, pos[1]), (pos[0]-1, pos[1]), (pos[0], pos[1]+1), (pos[0], pos[1]-1)):
        if 0 <= x2 < matrix.shape[0] and 0 <= y2 < matrix.shape[1] and (x2, y2) not in closed:
            if matrix[pos[0], pos[1]] + 1 >= matrix[x2, y2]:
                queue.append((x2, y2))

    return queue


def backtracking(closed, start, end):
    path = [end]
    while path[-1] != start:
        path.append(closed[path[-1]])

    return len(path)-1


def bfs(matrix, start, end):
    closed = {}
    closed[start] = None

    open = [start]
    while open:
        node = open.pop(0)
        if (node[0], node[1]) == end:
            return backtracking(closed, start, end)
        else:
            open += get_neighbours(matrix, node, end, closed)
            for adjacent in open:
                if adjacent not in closed:
                    closed[adjacent] = node


def fewestSteps(text):
    with open(text, 'r') as file:
        data = [[*x.strip()] for x in file.readlines()]
        for i, line in enumerate(data):
            data[i] = [ord(x) for x in line]
        matrix = np.array(data)

        start = np.where(matrix == 83)
        end = np.where(matrix == 69)

        matrix[start] = ord('a')
        matrix[end] = ord('z')

        start = np.where(matrix == ord('a'))

        best = np.inf
        for x in zip(start[0], start[1]):
            temp = bfs(matrix, (x[0], x[1]), (int(end[0]), int(end[1])))
            if temp != None and best > temp:
                best = temp

        return best


if '__main__' == __name__:
    print(fewestSteps('Day12.txt'))
