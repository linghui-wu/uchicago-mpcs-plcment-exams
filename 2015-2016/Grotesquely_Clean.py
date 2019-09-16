import sys

def grotesquely_clean(clean_list):
    if 6 in clean_list:
        print('CLEAN')
    elif sum(clean_list) >= 30:
        print('CLEAN')
    else:
        print('DO NOT CLEAN')

def main():
    contents = sys.stdin.readlines()

    clean_list = []
    for i in contents[0].split(' '):
        clean_list.append(int(i))

    grotesquely_clean(clean_list)


if __name__ == '__main__':
    main()

