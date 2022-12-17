from scipy.spatial import distance


def obtainPosition(sensors, size):

    checked = set()

    for point, value in sensors.items():
        for side in range(4):
            for i in range(value+1):
                if side == 0:
                    beaX = point[0] + value + 1 - i
                    beaY = point[1] - i
                elif side == 1:
                    beaX = point[0] - value - 1 + i
                    beaY = point[1] - i
                elif side == 2:
                    beaX = point[0] - value - 1 + i
                    beaY = point[1] + i     
                else:
                    beaX = point[0] + value + 1 - i
                    beaY = point[1] + i                       

                if (0 <= beaX < size and 0 <= beaY < size) and (beaX, beaY) not in checked:
                    found = all(distance.cityblock((beaX, beaY), otherPoint) > otherValue for otherPoint, otherValue in sensors.items())
                    if found:
                        return size * beaX + beaY
                checked.add((beaX, beaY))

    # for point, value in sensors.items():
    #     beaX, beaY = beacons[point]
    #     if size == beaY:
    #         existBeacon.add(beaX)
    #     if (dist := value - abs(size - point[1])) >= 0:
    #         noExistBeacon.update([x for x in range(point[0]-dist, point[0]+dist+1)])

    # noExistBeacon.difference_update(existBeacon)

    # return len(noExistBeacon)


def ContainBeacon(text, size):

    file = open(text, 'r')
    data = [x.strip() for x in file.readlines()]

    sensors = dict()
    for lines in data:
        lines = lines.replace('=', ' ').replace(':', '').replace(',', '')
        pos = lines.split(' ')
        sensX, sensY = int(pos[3]), int(pos[5])
        beaX, beaY = int(pos[11]), int(pos[13])
        sensors[(sensX, sensY)] = distance.cityblock((sensX, sensY), (beaX, beaY))

    return obtainPosition(sensors, size)


if '__main__' == __name__:
    print(ContainBeacon('Day_15/Day15.txt', 4_000_000))

