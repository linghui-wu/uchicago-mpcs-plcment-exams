import sys


def can_attack(point1, point2):
    flag = False

    b1 = point1[1] - point1[0]
    b2 = point1[1] + point1[0]

    if point1[0] == point2[0]:
        flag = True
    elif point1[1] == point2[1]:
        flag = True
    elif (point2[1] - point2[0]) == b1:
        flag = True
    elif (point2[1] + point2[0]) == b2:
        flag = True

    return flag


def main():
    # f = open('input.txt')
    # contents = f.readlines()
    # f.close()

    contents = sys.stdin.readlines()

    N = int(contents[0].rstrip('\n'))

    # to get all the coordinates and to store them in a list
    points = []
    point = []
    for coordinate in contents[1:]:
        x, y = int(coordinate.split(' ')[0]), int(coordinate.split(' ')[1].rstrip())
        point.append(x)
        point.append(y)
        points.append(point)
        point = []
    # print(points)

    judge_list = []

    for i in range(N):
        for j in range(i + 1, N):
            # print(points[i], points[j])
            if can_attack(points[i], points[j]):
                judge_list.append('INCORRECT')
            else:
                judge_list.append('CORRECT')
        #     print('({}, {})'.format(i, j), end = ' ')
        # print('\n')
    if 'INCORRECT' in judge_list:
        print('INCORRECT')
    else:
        print('CORRECT')


if __name__ == '__main__':
    main()

