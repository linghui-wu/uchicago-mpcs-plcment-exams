import sys


def c_g_ratio(c_num, g_num, a_num, t_num):
    try:
        return 100 * (c_num + g_num) / (c_num + g_num + a_num + t_num)
    except ZeroDivisionError:
        pass


def main():

    c_num = 0
    g_num = 0
    a_num = 0
    t_num = 0

    contents = sys.stdin.readlines()
    # row_num = int(contents[0])

    for row in contents[1:]:
        for base in row:
            if base == 'C':
                c_num += 1
            elif base == 'G':
                g_num += 1
            elif base == 'A':
                a_num += 1
            elif base == 'T':
                t_num += 1
            else:
                continue

    print(c_g_ratio(c_num, g_num, a_num, t_num))


if __name__ == '__main__':
    main()

