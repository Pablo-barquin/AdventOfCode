import numpy as np


def doMovement(value, steps, rope, positions):
    for i in range(steps):
        rope[0] += value
        for x, tail in enumerate(rope[1:]):
            if any(abs(rope[x]-tail) > 1) and any(abs(rope[x]-tail) == 0):
                tail += np.sign(rope[x]-tail)
            elif any(abs(rope[x]-tail) > 1):
                tail += np.sign(rope[x]-tail)
        if rope[-1].tolist() not in positions:
            positions.append(rope[-1].tolist())

    return rope


def positionsTailVisit(text):

    movements = {'R': [0, 1], 'L': [0, -1], 'U': [1, 0], 'D': [-1, 0]}
    rope = np.array([[0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
                     [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]])
    positions = [[0, 0]]

    with open(text, 'r') as file:
        data = file.readlines()
        data = [x.strip() for x in data]

        for x in data:
            move = x.split(' ')
            rope = doMovement(movements[move[0]], int(
                move[1]), rope, positions)

        return len(positions)


if '__main__' == __name__:
    print(positionsTailVisit('Day_9/Day9.txt'))
