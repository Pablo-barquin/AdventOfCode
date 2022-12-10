import numpy as np


def doMovement(value, steps, head, tail, positions):
    for i in range(steps):
        head += value
        if any(abs(head-tail) > 1) and any(abs(head-tail) == 0):
            tail += value
        elif any(abs(head-tail) > 1):
            tail += np.sign(head-tail)
        if tail.tolist() not in positions:
            positions.append(tail.tolist())

    return head, tail


def positionsTailVisit(text):

    movements = {'R': [0, 1], 'L': [0, -1], 'U': [1, 0], 'D': [-1, 0]}
    head = np.array([0, 0])
    tail = np.array([0, 0])
    positions = [[0, 0]]

    with open(text, 'r') as file:
        data = file.readlines()
        data = [x.strip() for x in data]

        for x in data:
            move = x.split(' ')
            head, tail = doMovement(movements[move[0]], int(
                move[1]), head, tail, positions)

        return len(positions)


if '__main__' == __name__:
    print(positionsTailVisit('Day_9/Day9.txt'))
