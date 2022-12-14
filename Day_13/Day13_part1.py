import ast


def checkPair(x, y):

    for pos in range(min([len(x), len(y)])):
        if isinstance(x[pos], int) and isinstance(y[pos], int):
            flag = x[pos] < y[pos] if x[pos] != y[pos] else 'None'
        elif isinstance(x[pos], list) and isinstance(y[pos], list):
            flag = checkPair(x[pos], y[pos])
        else:
            if isinstance(x[pos], int):
                x_aux = [x[pos]]
                y_aux = y[pos]
            else:
                x_aux = x[pos]
                y_aux = [y[pos]]
            flag = checkPair(x_aux, y_aux)
        if flag != 'None':
            return flag

    return len(x) < len(y) if len(x) != len(y) else 'None'


def sumIndicesPairs(text):

    with open(text, 'r') as file:
        data = [ast.literal_eval(x.strip())
                for x in file.readlines() if x != '\n']

        solution = list()
        it = 1
        while data:
            v1, v2 = data[0], data[1]
            if checkPair(v1, v2):
                solution.append(it)
            it += 1
            data = data[2:]

        return sum(solution)


if '__main__' == __name__:
    print(sumIndicesPairs('Day13.txt'))
