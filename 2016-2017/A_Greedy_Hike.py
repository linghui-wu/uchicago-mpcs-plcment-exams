import sys


def greedy_hiking(x, y, x_s, y_s, map):
    e = 0
    # print(x, y, x_s, y_s)
    if (x == 1) & (y == 1):
        x_s, y_s = 0, 0
        e = 0
        # print('e:{}, x_s:{}, y_s:{}'.format(e, x_s, y_s))

    elif (x == 1) & (y > 1):
        for i in range(y_s, y - 1):
            e += abs(map[x_s][y_s + 1] - map[x_s][y_s])
            # print('e:{}, x_s:{}, y_s:{}'.format(e, x_s, y_s))
        x_s, y_s = 0, (y - 1)

    elif (x > 1) & (y == 1):
        x_s, y_s = x_s, 0
        e = 0
        # print('e:{}, x_s:{}, y_s:{}'.format(e, x_s, y_s))

    elif (x > 1) & (y > 1):
        # for i in range(x_s, x):
        for j in range(y_s, y - 1):
            if y_s < (y - 1):

                # top line
                if (x_s == 0) & (0 <= y_s < (y - 1)):
                    if abs(map[0][y_s + 1] - map[x_s][y_s]) <= abs(map[1][y_s + 1] - map[x_s][y_s]):
                        e += abs(map[0][y_s + 1] - map[x_s][y_s])
                        x_s, y_s = 0, (y_s + 1)
                    else:
                        e += abs(map[1][y_s + 1] - map[x_s][y_s])
                        x_s, y_s = 1, (y_s + 1)
                    # print('e:{}, x_s:{}, y_s:{}'.format(e, x_s, y_s))

                # bottom line
                elif (x_s == (x - 1)) & (0 <= y_s < (y - 1)):
                    if abs(map[x - 2][y_s + 1] - map[x_s][y_s]) <= abs(map[x - 1][y_s + 1] - map[x_s][y_s]):
                        e += abs(map[x - 2][y_s + 1] - map[x_s][y_s])
                        x_s, y_s = (x - 2), (y_s + 1)
                    else:
                        e += abs(map[x - 1][y_s + 1] - map[x_s][y_s])
                        x_s, y_s = (x - 1), (y_s + 1)
                    # print('e:{}, x_s:{}, y_s:{}'.format(e, x_s, y_s))

                # others
                elif (0 < x_s < (x - 1)) & (0 <= y_s < (y - 1)):
                    e1 = abs(map[x_s - 1][y_s + 1] - map[x_s][y_s])
                    e2 = abs(map[x_s][y_s + 1] - map[x_s][y_s])
                    e3 = abs(map[x_s + 1][y_s + 1] - map[x_s][y_s])
                    if (e1 < e2) & (e1 <= e3):
                        e += e1
                        x_s, y_s = (x_s - 1), (y_s + 1)
                    elif (e2 <= e1) & (e2 <= e3):
                        e += e2
                        x_s, y_s = x_s, (y_s + 1)
                    elif (e3 < e1) & (e3 < e2):
                        e += e3
                        x_s, y_s = (x_s + 1), (y_s + 1)
                    # print('e:{}, x_s:{}, y_s:{}'.format(e, x_s, y_s))

    return [x_s, y_s, e]


def main():
    # f = open('input.txt')
    # contents = f.readlines()
    # f.close()

    contents = sys.stdin.readlines()

    # to get the number of lines(x) and the number of rows(y)
    x, y = int(contents[0].split(' ')[0]), int(contents[0].split(' ')[1].rstrip('\n'))

    # to get the starting position (x_s, y_s)
    x_s, y_s = int(contents[1].split(' ')[0]), int(contents[1].split(' ')[1].rstrip('\n'))

    # to obtain the mountain
    map = []
    line = []
    for i in contents[2:]:
        for j in i.split(' '):
            line.append(int(j.rstrip('\n')))
        map.append(line)
        line = []

    # print(greedy_hiking(x, y, x_s, y_s, map))
    result_list = greedy_hiking(x, y, x_s, y_s, map)
    for i in result_list:
        print(i, end = ' ')


if __name__ == '__main__':
    main()

