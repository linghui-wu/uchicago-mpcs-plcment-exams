import sys


def exponentiation_by_squaring(x, n):
    if n == 0:
        result = 1
    elif n == 1:
        result = x
    elif (n > 1) & (n % 2 == 0):
        result = exponentiation_by_squaring(x * x, n / 2)
    elif (n > 1) & (n % 2 == 1):
        result = exponentiation_by_squaring(x * x, (n - 1) / 2) * x

    return result

def main():
    contents = sys.stdin.readlines()

    x, n = int(contents[0].split(' ')[0]), int(contents[0].split(' ')[1].rstrip('\n'))
    print(exponentiation_by_squaring(x, n))


if __name__ == '__main__':
    main()

