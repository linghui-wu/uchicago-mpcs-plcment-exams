import sys


def solve_minefield(mine_field, x, y):

    solved_mine_field = []
    row = []

    for i in range(len(mine_field)):
        # print(mine_field[i])
        for j in range(len(mine_field[i])):
            # print(type(mine_field[i][j]))

            # to print the mine
            if mine_field[i][j] == 1:
                row.append('X')

            elif mine_field[i][j] != 1: #如果没有雷，进行分类讨论
                count = 0
                if (x > 1) & (y > 1):
                    # 左上角
                    if (i == 0) & (j == 0):
                        if mine_field[1][0] == 1:
                            count += 1
                        if mine_field[1][1] == 1:
                            count += 1
                        if mine_field[0][1] == 1:
                            count += 1
                    # 右上角
                    elif (i == 0) & (j == (y - 1)):
                        if mine_field[0][y - 2] == 1:
                            count += 1
                        if mine_field[1][y - 2] == 1:
                            count += 1
                        if mine_field[1][y - 1] == 1:
                            count += 1
                    # 左下角
                    elif (i == (x - 1)) & (j == 0):
                        if mine_field[x - 2][0] == 1:
                            count += 1
                        if mine_field[x - 2][1] == 1:
                            count += 1
                        if mine_field[x - 1][1] == 1:
                            count += 1
                    # 右下角
                    elif (i == (x - 1)) & (j == (y - 1)):
                        if mine_field[x - 1][y - 2] == 1:
                            count += 1
                        if mine_field[x - 2][y - 2] == 1:
                            count += 1
                        if mine_field[x - 2][y - 1] == 1:
                            count += 1
                    # 左边
                    elif (0 < i < (x - 1)) & (j == 0):
                        if mine_field[i - 1][0] == 1:
                            count += 1
                        if mine_field[i - 1][1] == 1:
                            count += 1
                        if mine_field[i][1] == 1:
                            count += 1
                        if mine_field[i + 1][1] == 1:
                            count += 1
                        if mine_field[i + 1][0] == 1:
                            count += 1
                    # 右边
                    elif (0 < i < (x - 1)) & (j == (y - 1)):
                        if mine_field[i - 1][y - 2] == 1:
                            count += 1
                        if mine_field[i - 1][y - 1] == 1:
                            count += 1
                        if mine_field[i][y - 2] == 1:
                            count += 1
                        if mine_field[i + 1][y - 2] == 1:
                            count += 1
                        if mine_field[i + 1][y - 1] == 1:
                            count += 1
                    # 上边
                    elif (i == 0) & (0 < j < (y - 1)):
                        if mine_field[0][j - 1] == 1:
                            count += 1
                        if mine_field[0][j + 1] == 1:
                            count += 1
                        if mine_field[1][j - 1] == 1:
                            count += 1
                        if mine_field[1][j] == 1:
                            count += 1
                        if mine_field[1][j + 1] == 1:
                            count += 1
                    # 下边
                    elif (i == (x - 1)) & (0 < j < (y - 1)):
                        if mine_field[x - 2][j] == 1:
                            count += 1
                        if mine_field[x - 2][j - 1] == 1:
                            count += 1
                        if mine_field[x - 2][j + 1] == 1:
                            count += 1
                        if mine_field[x - 1][j - 1] == 1:
                            count += 1
                        if mine_field[x - 1][j + 1] == 1:
                            count += 1
                    # 其他部分
                    elif (0 < i < (x - 1)) & (0 < j < (y - 1)):
                        if mine_field[i - 1][j - 1] == 1:
                            count += 1
                        if mine_field[i][j - 1] == 1:
                            count += 1
                        if mine_field[i + 1][j - 1] == 1:
                            count += 1
                        if mine_field[i - 1][j] == 1:
                            count += 1
                        if mine_field[i + 1][j] == 1:
                            count += 1
                        if mine_field[i - 1][j + 1] == 1:
                            count += 1
                        if mine_field[i][j + 1] == 1:
                            count += 1
                        if mine_field[i + 1][j + 1] == 1:
                            count += 1

                    if count == 0:
                        row.append('-')
                    else:
                        row.append(count)

                elif (x == 1) & (y > 1):
                    # 左顶点
                    if j == 0:
                        if mine_field[0][1] == 1:
                            count += 1
                    # 右顶点
                    elif j == (y - 1):
                        if mine_field[0][y - 2] == 1:
                            count += 1
                    # 中间点
                    else:
                        if mine_field[0][j - 1] == 1:
                            count += 1
                        if mine_field[0][j + 1] == 1:
                            count += 1

                    if count == 0:
                        row.append('-')
                    else:
                        row.append(count)
                elif (x > 1) & (y == 1):
                    # 上顶点
                    if i == 0:
                        if mine_field[1][0] == 1:
                            count += 1
                    # 下顶点
                    elif i == (x - 1):
                        if mine_field[x - 2][0] == 1:
                            count += 1
                    # 中间点
                    else:
                        if mine_field[i - 1][0] == 1:
                            count += 1
                        if mine_field[i + 1][0] == 1:
                            count += 1
                    if count == 0:
                        row.append('-')
                    else:
                        row.append(count)
                elif (x == 1) & (y == 1):
                    count = 0

                    if count == 0:
                        row.append('-')
                    else:
                        row.append(count)



        solved_mine_field.append(row)
        row = []

    for i in range(len(solved_mine_field)):
        for j in range(len(solved_mine_field[i])):
            print(solved_mine_field[i][j], end = '')
        print(' ')



def main():
    # f = open('input.txt')
    # contents = f.readlines()
    # f.close()

    contents = sys.stdin.readlines()

    # to obtain the number of rows(x) and the number of columns(y)
    x, y = int(contents[0].split(' ')[0]), int(contents[0].split(' ')[1].rstrip('\n'))
    # print(x, y)

    mine_field = []
    row = []

    # to obtain the mine field
    for i in contents[1:]:
        # print(i.split(' '))
        for j in i.split(' '):
            row.append(int(j.rstrip('\n')))
        mine_field.append(row)
        row = []
    # print(mine_field)


    # to obtain the coordinates of the mine field
    # for i in range(len(mine_field)):
    #     for j in range(len(mine_field[i])):
    #         print('(' + str(i) + ',' + str(j) + ')', end = ' ')
    #     print('\n')

    solve_minefield(mine_field, x, y)


if __name__ == '__main__':
    main()

