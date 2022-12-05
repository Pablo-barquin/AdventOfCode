
def crateMover_9000(steps, origin, destiny, crates):

    for it in range(steps):
        crates[destiny].insert(0, crates[origin][0])
        crates[origin].pop(0)


def obtainStacks(text):

    stacks = {}
    it = 0
    endLine = 0
    with open(text, 'r') as file:
        line = file.readline()
        while line != '\n':
            for it in range(0, len(line)//4):
                if str(it+1) not in stacks:
                    stacks[str(it+1)] = []
                if line[4*it] == '[':
                    stacks[str(it+1)].append(line[(4*it)+1])
            line = file.readline()
            endLine += 1
        file.close()

    return stacks, endLine


def topOfEachStack(text):

    stacks, endLine = obtainStacks(text)
    with open(text, 'r') as file:
        for x, line in enumerate(file):
            if x > endLine:
                line = line.replace('\n', '').split(' ')
                crateMover_9000(int(line[1]), line[3], line[5], stacks)

    return stacks


if '__main__' == __name__:
    stack = topOfEachStack('Day_5/Day5.txt')
    for value in stack.values():
        print(value[0], end='')
