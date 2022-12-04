
def mostCaloriesElf(text):

    Elfs = []
    with open(text, 'r') as file:
        Acum = 0
        for lines in file:
            if lines == '\n':
                Elfs.append(Acum)
                Acum = 0
            else:
                Acum += int(lines)

    print(sum(sorted(Elfs, reverse=True)[0:3]))

if '__main__' == __name__:
    mostCaloriesElf('Day1.txt')