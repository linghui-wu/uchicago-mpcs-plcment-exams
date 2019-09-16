import sys


def GCD(a, b):
    if a == b:
        gcd = a
    elif a > b:
        gcd = GCD(a - b, a)
    elif a < b:
        gcd = GCD(a, b - a)

    return gcd


def main():
    contents = sys.stdin.readlines()

    a, b = int(contents[0].split(' ')[0]), int(contents[0].split(' ')[1].rstrip('\n'))
    print(GCD(a, b))


if __name__ == '__main__':
    main()

