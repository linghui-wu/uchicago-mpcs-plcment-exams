import sys


def name_equivalence(name):
    equal_name_list = []

    if len(name) == 1:
        equal_name_list.append(name[0])
    elif len(name) % 2 == 0:
        for i in range(1, len(name), 2):
            equal_name_list.append(name[i])
            equal_name_list.append(name[i - 1])
    elif (len(name) > 1) & (len(name) % 2 == 1):
        for i in range(1, len(name), 2):
            equal_name_list.append(name[i])
            equal_name_list.append(name[i -1])
        equal_name_list.append(name[-1])

    equal_name_str = ''
    for i in equal_name_list:
        equal_name_str += i

    return equal_name_str


def main():
    contents = sys.stdin.readlines()

    name = contents[0].rstrip('\n')
    print(name_equivalence(name))


if __name__ == '__main__':
    main()

