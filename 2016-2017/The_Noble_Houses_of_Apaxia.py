import sys


def generate_noble_name(first_name, last_name):
    '''
    compute the noble name of the Apaxians
    '''
    if len(last_name) == 5:
        last_name *= 4
    else:
        last_name *= len(last_name)

    noble_name = first_name + ' ' + last_name
    return noble_name


def main():
    contents = sys.stdin.readlines()

    first_name, last_name = contents[0].split(' ')[0], contents[0].split(' ')[1].rstrip('\n')
    print(generate_noble_name(first_name, last_name))


if __name__ == '__main__':
    main()
