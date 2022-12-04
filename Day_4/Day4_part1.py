
def isFullyContain(numbers, range):

    for number in numbers:
        if number not in range:
            return False

    return True


def rangesAssigments(text):

    with open(text, 'r') as file:
        pairs = []
        for lines in file:
            lines = lines.replace('\n', '')
            for splitter in [',', '-']:
                lines = lines.replace(splitter, ' ')

            pairs.append(list((map(int, lines.split(' ')))))

        solution = sum([isFullyContain(x[:2], range(x[2], x[3]+1)) |
                       isFullyContain(x[2:], range(x[0], x[1]+1)) for x in pairs])

        return (solution)


if '__main__' == __name__:
    print(rangesAssigments('Day4.txt'))
