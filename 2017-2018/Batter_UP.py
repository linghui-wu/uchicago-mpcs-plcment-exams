import sys


def slugging_avg_cal(total_hits, at_bats):
    try:
        return float(total_hits/at_bats)
    except ZeroDivisionError:
        pass


def main():

    contents = sys.stdin.readlines()
    # f = open('input.txt')
    # contents = f.readlines()
    # f.close()

    plate_appearance_num = int(contents[0])
    plate_appearance = contents[1]

    plate_appearance_list = []

    for plate in plate_appearance.split(' '):
        plate_i = int(plate)

        if plate_i == -1:
            plate_appearance_num -= 1

        if plate_i != -1:
            plate_appearance_list.append(plate_i)

    total_hits = sum(plate_appearance_list)

    print(slugging_avg_cal(total_hits, plate_appearance_num))


if __name__ == '__main__':
    main()

