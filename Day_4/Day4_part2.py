
def isOverlap(numbers, range):

    for number in numbers:
        if number in range:
            return True

    return False


def rangesAssigments(text):

    with open(text, 'r') as file:
        pairs = []
        for lines in file:
            lines = lines.replace('\n', '')
            for splitter in [',', '-']:
                lines = lines.replace(splitter, ' ')

            pairs.append(list((map(int, lines.split(' ')))))

        solution = sum([isOverlap(x[:2], range(x[2], x[3]+1)) |
                       isOverlap(x[2:], range(x[0], x[1]+1)) for x in pairs])

        return (solution)


if '__main__' == __name__:
    print(rangesAssigments('Day4.txt'))
