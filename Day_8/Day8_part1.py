import numpy as np


def treesVisible(text):

    with open(text, 'r') as file:
        data = file.readlines()
        data = [list(x.strip()) for x in data]
        matrix = np.array(data)

        trees = 0
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[0]):
                trees += (all(matrix[i, j] > x for x in matrix[i, :j]) or all(matrix[i, j] > x for x in matrix[i, j+1:]) or 
                          all(matrix[i, j] > x for x in matrix[:i, j]) or all(matrix[i, j] > x for x in matrix[i+1:, j]))

        return trees


if '__main__' == __name__:
    print(treesVisible('Day8.txt'))
