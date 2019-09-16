import sys


def mccarthy_91_function(n):
    if n > 100:
        n -= 10
    else:
        n = mccarthy_91_function(mccarthy_91_function(n+11))

    return n


def main():
    contents = sys.stdin.readlines()

    n = int(contents[0].rstrip('\n'))
    print(mccarthy_91_function(n))


if __name__ == '__main__':
    main()

