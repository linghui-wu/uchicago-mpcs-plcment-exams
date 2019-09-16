import sys

global point

def shot_ship(shot, ship_list):
    is_shot = False
    for i in ship_list:
        if (shot[0] == i[0]) & (shot[1] == i[1]):
            is_shot = True
            ship_list.remove(i)
    return is_shot

def shot_water(shot, ship_list):
    miss = True
    for i in ship_list:
        if shot_ship(shot, ship_list):
            miss = False
    dist = []
    if miss:
        for i in ship_list:
            manhatten_distance = abs(shot[0] - i[0]) + abs(shot[1] - i[1])
            dist.append(manhatten_distance)
    D = min(dist)
    return D

def main():
    # f = open('input.txt')
    # contents = f.readlines()
    # f.close()

    contents = sys.stdin.readlines()

    N, M, S, R = int(contents[0].split(' ')[0]), int(contents[0].split(' ')[1]), int(contents[0].split(' ')[2]), int(contents[0].split(' ')[3])
    # print(N, M, S, R)

    # to get the list of ship coordinates
    ship_list = []
    for i in contents[1: S + 1]:
        ship = []
        for j in i.split(' '):
            ship.append(int(j.rstrip('\n')))
        ship_list.append(ship)
    # print(ship_list)

    # to get the list of shot coordinates
    shot_list = []
    for i in contents[S + 1:]:
        shot = []
        for j in i.split(' '):
            shot.append(int(j.rstrip('\n')))
        shot_list.append(shot)
    # print(shot_list)

    point = 0
    H = 0

    for shot in shot_list:
        if shot_ship(shot, ship_list):
            point += 1000
            H += 1
        else:
            point += max(0, 1000 - (shot_water(shot, ship_list) * 100))

    # no need to simplify the fraction
    print('{}/{} ships sunk. Score: {} points'.format(H, S, point))

if __name__ == '__main__':
    main()

