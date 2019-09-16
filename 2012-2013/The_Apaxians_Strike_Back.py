import sys


def first_letter_num(name):
    '''
        To determine how important the name is - how many times the first letter of the name appears in the name
    '''

    first_letter = name[0]
    count = 0

    for i in name:
        if i == first_letter:
            count += 1
        else:
            continue
    return count


def main():
    contents = sys.stdin.readlines()

    name = contents[0].rstrip('\n')
    print(first_letter_num(name))

if __name__ == '__main__':
    main()

