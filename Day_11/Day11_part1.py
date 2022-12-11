
def aritmeticOperation(item, sign, number):
    if number == 'old':
        number = item
    if sign == '+':
        return item + int(number)
    elif sign == '*':
        return item * int(number)


def inspectedItems(monkeys):
    items = [0] * len(monkeys)
    for _ in range(20):
        for number, monkey in monkeys.items():
            while len(monkey['items']):
                new = (aritmeticOperation(
                    monkey['items'][0], monkey['op']['sign'], monkey['op']['number']))//3
                monkeys[monkey[new % monkey['test'] == 0]]['items'].append(new)
                monkey['items'].pop(0)
                items[number] += 1

    return items


def saveInfoMonkey(data):
    dictMonkeys = {}
    number = 0
    while len(data) > 0:
        lines = data[1:6]
        data = data[7:]
        monkey = {'items': [], 'op': {'sign': '', 'number': 0},
                  'test': 0, True: 0, False: 0}
        monkey['items'] = [int(x) for x in lines[0][2:]]
        monkey['op']['sign'] = lines[1][4]
        monkey['op']['number'] = lines[1][-1]
        monkey['test'] = int(lines[2][-1])
        monkey[True] = int(lines[3][-1])
        monkey[False] = int(lines[4][-1])

        dictMonkeys[number] = monkey
        number += 1

    return dictMonkeys


def levelMonkeyBusiness(text):

    with open(text, 'r') as file:
        rawData = [x.strip().replace(',', '').split(' ')
                   for x in file.readlines()]
        dictMonkeys = saveInfoMonkey(rawData)
        items = inspectedItems(dictMonkeys)

        return sorted(items)[-1] * sorted(items)[-2]


if '__main__' == __name__:
    print(levelMonkeyBusiness('Day11.txt'))
