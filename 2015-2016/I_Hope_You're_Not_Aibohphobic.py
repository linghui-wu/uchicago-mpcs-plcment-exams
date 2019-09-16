import sys

def is_palindrome(word):
    '''
    to detect whether a word is a palindrome using a recursive function
    '''
    flag = False
    if len(word) == 1:
        flag = True
    elif len(word) == 2:
        if word[0] == word[1]:
            flag = True
    elif (word[0] == word[-1]) and is_palindrome(word[1:-1]):
        flag = True

    return flag


def main():
    contents = sys.stdin.readlines()

    word = contents[0].rstrip('\n')
    # print(word)

    if is_palindrome(word):
        print('PALINDROME')
    else:
        print('NOT PALINDROME')

if __name__ == '__main__':
    main()

