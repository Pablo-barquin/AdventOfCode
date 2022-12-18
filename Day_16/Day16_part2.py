import numpy as np
from itertools import product, combinations
from collections import defaultdict

# Helped by GITHUB: mebeim/aoc


def floyd(G):
    dist = defaultdict(lambda: defaultdict(lambda: np.inf))

    for ax, path in G.items():
        dist[ax][ax] = 0
        for bx in path:
            dist[ax][bx] = 1

    for ax, bx, cx in product(G, G, G):
        bc, ba, ac = dist[bx][cx], dist[bx][ax], dist[ax][cx]

        if ba + ac < bc:
            dist[bx][cx] = ba + ac

    return dist


def solutions(distance, pressure, valvules, time=30, cur='AA', chosen={}):
    for nxt in valvules:
        new_time = time - distance[cur][nxt] - 1
        if new_time < 2:
            continue
        new_chosen = chosen.copy()
        new_chosen.update({nxt: new_time})
        new_valves = valvules - {nxt}
        yield from solutions(distance, pressure, new_valves, new_time, nxt, new_chosen)

    yield chosen


def final_score(pressure, chosen_val):
    sol = 0
    for valvule, time in chosen_val.items():
        sol += pressure[valvule] * time
    return sol


def mostPressure(text):

    file = open(text, 'r')
    data = [x.strip() for x in file.readlines()]

    nodes = defaultdict()
    pressure = dict()
    for line in data:
        line = line.replace('=', ' ').replace(';', '').replace(',', '').split(' ')
        val, flow, path = line[1], line[5], line[10:]
        nodes[val] = path
        pressure[val] = int(flow)

    distances = floyd(nodes)
    valvules = set(filter(pressure.get, nodes.keys()))

    best = 0
    maxscore = defaultdict(int)
    for path in solutions(distances, pressure, valvules, 26):
        k = frozenset(path)
        sol = final_score(pressure, path)
        
        if sol > maxscore[k]:
            maxscore[k] = sol

    for (s1, score1), (s2, score2) in combinations(maxscore.items(), 2):
        if len(s1 & s2) == 0:
            cur = score1 + score2
            if cur > best:
                best = cur

    return best


if '__main__' == __name__:
    print(mostPressure('Day16.txt'))
