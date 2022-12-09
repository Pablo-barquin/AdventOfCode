import numpy as np


def pointsTrees(number, arr, inverse=False):

    if inverse:
        return next((x+1 for x, val in enumerate(arr[::-1]) if val >= number), len(arr))
    else:
        return next((x+1 for x, val in enumerate(arr) if val >= number), len(arr))


def highestScenicScore(text):

    with open(text, 'r') as file:
        data = file.readlines()
        data = [list(x.strip()) for x in data]
        matrix = np.array(data)

        best_score = 0
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[0]):
                score = pointsTrees(matrix[i, j], matrix[i, :j], True) * pointsTrees(matrix[i, j], matrix[i, j+1:]) * pointsTrees(
                    matrix[i, j], matrix[:i, j], True) * pointsTrees(matrix[i, j], matrix[i+1:, j])
                if score > best_score:
                    best_score = score

        return best_score


if '__main__' == __name__:
    print(highestScenicScore('Day8.txt'))
