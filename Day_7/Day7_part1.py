
def checkInstructions(input, path):

    directory = []
    while len(input):
        line = input[0].split(' ')
        if '$' in line:
            if 'cd' in line and '..' in line:
                directory.pop()
            elif 'cd' in line:
                directory.append(line[-1])
                path['/'.join(directory)] = 0
        else:
            if line[0].isnumeric():
                temp_directory = directory.copy()
                while len(temp_directory):
                    path['/'.join(temp_directory)] += int(line[0])
                    temp_directory.pop()
        input.pop(0)


def SizeDirectories(text):

    with open(text, 'r') as file:
        lines = file.readlines()
        lines = [x.strip() for x in lines]
        if '$ cd /' in lines[0]:
            path = dict()
            checkInstructions(lines, path)
        else:
            return 0

    return sum(v for v in path.values() if v < 100000)


if '__main__' == __name__:
    print(SizeDirectories('Day7.txt'))
