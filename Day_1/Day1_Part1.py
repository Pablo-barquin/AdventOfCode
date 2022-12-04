
def mostCaloriesElf(text):

    elfs = []
    with open(text, 'r') as file:
        sum = 0
        for lines in file:
            if lines == '\n':
                elfs.append(sum)
                sum = 0
            else:
                sum += int(lines)

    return max(elfs)


if '__main__' == __name__:
    print(mostCaloriesElf('Day1.txt'))
