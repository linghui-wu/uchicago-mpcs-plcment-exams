import sys

def codex_mendax(community_name, name_list):

    princess_num = 0
    baron_num = 0
    priest_num = 0
    commoner_num = 0

    for i in name_list:
        if i[:len(community_name)] == community_name:
            princess_num += 1
        elif i[-len(community_name):] == community_name:
            baron_num += 1
        elif community_name in i[1:-1]:
            priest_num += 1
        else:
            commoner_num += 1

    return [princess_num, baron_num, priest_num, commoner_num]


def main():
    contents = sys.stdin.readlines()

    community_name, name_num = contents[0].rstrip('\n'), int(contents[1])

    name_list = []

    for i in contents[2:]:
        name_list.append(i.rstrip('\n'))

    num_list = codex_mendax(community_name, name_list)

    print('{} PRINCESS\n{} BARON\n{} PRIEST\n{} COMMONER'.format(num_list[0], num_list[1], num_list[2], num_list[3]))


if __name__ == '__main__':
    main()

