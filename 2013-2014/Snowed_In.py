import sys

def main():
    contents = sys.stdin.readlines()

    snow_depth_list = []
    for i in contents[1].rstrip('\n').split(' '):
        snow_depth_list.append(int(i))

    print(max(snow_depth_list) - min(snow_depth_list))


if __name__ == '__main__':
    main()


