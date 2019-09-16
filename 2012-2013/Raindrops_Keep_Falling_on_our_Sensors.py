import sys


def average_rainfall(n, measurement_list):
    rainfall_sum = 0

    for i in measurement_list:
        if i < 0:
            n -= 1
            continue
        else:
            rainfall_sum += i

    if n == 0:
        print('INSUFFICIENT DATA')
    else:
        print(int(rainfall_sum / n))

def main():
    contents = sys.stdin.readlines()
    # f = open('input.txt')
    # contents = f.readlines()
    # f.close()

    measurement_list = []

    n = int(contents[0])
    for i in contents[1].rstrip('\n').split(' '):
        measurement_list.append(int(i))

    average_rainfall(n, measurement_list)


if __name__ == '__main__':
    main()

