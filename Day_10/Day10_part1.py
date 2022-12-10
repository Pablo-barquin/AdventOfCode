
def executionCycle(data):
    cycle = 0
    signals = []
    registerX = 1
    mark = 20
    while cycle <= 220:
        line = data[0].split(' ')
        if line[0] == 'noop':
            cycle += 1
        else:
            for i in range(2):
                cycle += 1
                if cycle == mark:
                    signals.append(registerX*mark)
                    mark += 40
            registerX += int(line[-1])
        if cycle == mark:
            signals.append(registerX*mark)
            mark += 40
        data.pop(0)

    return signals


def signalStrengths(text):

    with open(text, 'r') as file:
        data = [x.strip() for x in file.readlines()]
        signals = executionCycle(data)

        file.close()

    return sum(signals)


if '__main__' == __name__:
    print(signalStrengths('Day10.txt'))
