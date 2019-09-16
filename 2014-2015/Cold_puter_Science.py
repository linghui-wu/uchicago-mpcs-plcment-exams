import sys


def number_of_cold_days(total_days, temperature_list):
    cold_days_num = 0

    for i in range(total_days):
        if temperature_list[i] < 0:
            cold_days_num += 1

    return cold_days_num


def main():
    contents = sys.stdin.readlines()

    total_days = int(contents[0])
    # print('total_days: ', total_days)
    temperature_list = []

    for i in contents[1].rstrip('\n').split(' '):
        temperature_list.append(int(i))

    print(number_of_cold_days(total_days, temperature_list))


if __name__ == '__main__':
    main()

