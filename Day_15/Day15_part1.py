from scipy.spatial import distance


def obtainPositions(sensors, beacons, row):

    existBeacon = set()
    noExistBeacon = set()

    for point, value in sensors.items():
        beaX, beaY = beacons[point]
        if row == beaY:
            existBeacon.add(beaX)
        if (dist := value - abs(row - point[1])) >= 0:
            noExistBeacon.update([x for x in range(point[0]-dist, point[0]+dist+1)])

    noExistBeacon.difference_update(existBeacon)

    return len(noExistBeacon)


def cannotContainBeacon(text, row):

    file = open(text, 'r')
    data = [x.strip() for x in file.readlines()]

    sensors = dict()
    beacons = dict()
    for lines in data:
        lines = lines.replace('=', ' ').replace(':', '').replace(',', '')
        pos = lines.split(' ')
        sensX, sensY = int(pos[3]), int(pos[5])
        beaX, beaY = int(pos[11]), int(pos[13])
        sensors[(sensX, sensY)] = distance.cityblock((sensX, sensY), (beaX, beaY))
        beacons[(sensX, sensY)] = (beaX, beaY)

    return obtainPositions(sensors, beacons, row)


if '__main__' == __name__:
    print(cannotContainBeacon('Day_15/Day15.txt', 2000000))
