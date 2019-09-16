import sys


def name_convertor(name):
    '''
    to convert the Apaxian names into a more readable format
    '''

    simplified_name = name[0]

    for i in range(1, len(name)):
        # print(name[i])
        if name[i] != name[i-1]:
            simplified_name += name[i]

    return simplified_name


def main():
    contents = sys.stdin.readlines()

    name = contents[0].rstrip('\n')
    print(name_convertor(name))


if __name__ == '__main__':
    main()

