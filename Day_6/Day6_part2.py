
def firstStartOfMessageMarker(text):
    pass
    with open(text, 'r') as file:
        datastream = file.readline()
        buffer = datastream[:13]
        datastream = datastream[13:]
        it = 14
        while datastream[0] != '\n':
            buffer += datastream[0]
            if len(set(buffer)) == len(buffer):
                break
            else:
                buffer = buffer[1:]
                datastream = datastream[1:]
                it += 1

    return it


if '__main__' == __name__:
    print(firstStartOfMessageMarker('Day6.txt'))
