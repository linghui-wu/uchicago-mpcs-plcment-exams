import sys


def fill(index, list_a, old_value, new_value):

    if 0 <= index < len(list_a):
        if list_a[index] != old_value:
            return list_a
        elif list_a[index] == new_value:
            return list_a
        elif list_a[index] == old_value:
            list_a[index] = new_value
            fill(index - 1, list_a, old_value, new_value)
            fill(index + 1, list_a, old_value, new_value)
            return list_a


def main():
    contents = sys.stdin.readlines()

    N = int(contents[0].split(' ')[0])
    index = int(contents[0].split(' ')[1])
    x = int(contents[0].split(' ')[2].rstrip('\n'))

    list_a = []
    for i in contents[1].split(' '):
        list_a.append(int(i))

    old_value = list_a[index]
    new_value = x

    result_list = fill(index, list_a, old_value, new_value)
    for i in result_list:
        print(i, end = ' ')


if __name__ == '__main__':
    main()

