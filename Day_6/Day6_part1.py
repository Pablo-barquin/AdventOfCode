
def firstStartOfPacketMarker(text):
    pass
    with open(text, 'r') as file:
        datastream = file.readline()
        buffer = datastream[:3]
        datastream = datastream[3:]
        it = 4
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
    print(firstStartOfPacketMarker('Day6.txt'))
