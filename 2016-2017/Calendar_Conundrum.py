import sys


def date_format(a, b, c):
    '''
    the format of a given date or whether the format is ambigious
    '''

    if a > 31:
        print('Format #3')
    elif 12 < a <= 31:
        if c > 31:
            print('Format #2')
        else:
            print('Ambiguous')
    else:
        if b > 12:
            print('Format #1')
        else:
            print('Ambiguous')


def main():
    contents = sys.stdin.readlines()

    argus = contents[0].split(' ')
    a, b, c = int(argus[0]), int(argus[1]), int(argus[2])

    date_format(a, b, c)


if __name__ == '__main__':
    main()

