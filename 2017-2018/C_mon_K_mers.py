import sys


def k_mers(k, str):

    k_mers_dict = {}

    for i in range(len(str)):
        k_mers_dict[str[i:i + k]] = k_mers_dict.get(str[i:i+k], 0) + 1

    return k_mers_dict


def main():
    # f = open('input.txt')
    # contents = f.readlines()
    # f.close()

    contents = sys.stdin.readlines()

    # to obtain the arguments
    argus = contents[0].split(' ')
    L, N, k, Q = int(argus[0]), int(argus[1]), int(argus[2]), int(argus[3].rstrip('\n'))

    # to obtain the string
    str = ''
    for i in contents[1:-Q]:
        str += i.rstrip('\n')

    # to obtain the k-mers list for output
    k_mers_list = []
    for i in contents[-Q:]:
        k_mers_list.append(i.rstrip('\n'))

    result_dict = k_mers(k, str)
    # print(result_dict)

    for i in k_mers_list:
        if i in result_dict:
            print('{} {}'.format(i, result_dict[i]))
        else:
            print('{} {}'.format(i, 0))


if __name__ == '__main__':
    main()

