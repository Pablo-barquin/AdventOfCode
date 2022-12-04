
def mostCaloriesElf(text):

    elfs = []
    with open(text, 'r') as file:
        acum = 0
        for lines in file:
            if lines == '\n':
                elfs.append(acum)
                acum = 0
            else:
                acum += int(lines)

    print(sum(sorted(elfs, reverse=True)[0:3]))


if '__main__' == __name__:
    mostCaloriesElf('Day1.txt')
