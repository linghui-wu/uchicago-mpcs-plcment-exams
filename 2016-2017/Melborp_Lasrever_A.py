import sys


def reverse_str(str):
    '''
    reverse the string
    '''

    if len(str) == 1:
        str_result = str
    else:
        str_result = reverse_str(str[1:]) + str[0]

    return str_result


def main():

    contents = sys.stdin.readlines()
    str = contents[0]
    print(reverse_str(contents[0]))


if __name__ == '__main__':
    main()

