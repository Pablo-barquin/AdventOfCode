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


def partition(data, low, high):
    pivot = data[high]
    i = low - 1

    for j in range(low, high):
        if checkPair(data[j], pivot):
            i = i + 1

            (data[i], data[j]) = (data[j], data[i])

    (data[i + 1], data[high]) = (data[high], data[i + 1])
    return i + 1


def quick_sort(data, low, high):
    if low < high:
        pi = partition(data, low, high)
        quick_sort(data, low, high-1)
        quick_sort(data, pi+1, high)


def sumIndicesPairs(text):

    with open(text, 'r') as file:
        data = [ast.literal_eval(x.strip())
                for x in file.readlines() if x != '\n'] + [[[2]]] + [[[6]]]

        quick_sort(data, 0, len(data)-1)

        return (data.index([[2]]) + 1) * (data.index([[6]]) + 1)


if '__main__' == __name__:
    print(sumIndicesPairs('Day13.txt'))
