import sys


def reverse_polish_notation(token_list):
    operantor_list = ['+', '*', '==', 'and', 'or']
    stack_list = []

    for i in range(len(token_list)):
        if token_list[i].isnumeric():
            stack_list.append(int(token_list[i]))
        elif token_list[i] == 'true':
            stack_list.append(True)
        elif token_list[i] == 'false':
            stack_list.append(False)
        elif token_list[i] in operantor_list:
            # print('stack list before operation: ', stack_list)
            if len(stack_list) < 2:
                return 'SYNTAX ERROR'

            operand_1 = stack_list[-1]
            operand_2 = stack_list[-2]

            if type(operand_1) != type(operand_2):
                return 'TYPE ERROR'
            else:
                if (i in operantor_list[:3]) & (isinstance(operand_1, bool) | isinstance(operand_2, bool)):
                    return 'TYPE ERROR'
                elif (i in operantor_list[-2:]) & (isinstance(operand_1, int) | isinstance(operand_2, int)):
                    return 'TYPE ERROR'
                else:
                    if token_list[i] == operantor_list[0]:
                        result = operand_1 + operand_2
                        stack_list = stack_list[:-2] + [result]
                    elif token_list[i] == operantor_list[1]:
                        result = operand_1 * operand_2
                        stack_list = stack_list[:-2] + [result]
                    elif token_list[i] == operantor_list[2]:
                        result = (operand_1 == operand_2)
                        stack_list = stack_list[:-2] + [result]
                    elif token_list[i] == operantor_list[3]:
                        result = (operand_1 & operand_2)
                        stack_list = stack_list[:-2] + [result]
                    elif token_list[i] == operantor_list[4]:
                        result = (operand_1 | operand_2)
                        stack_list = stack_list[:-2] + [result]

    # print('stack list after operation:', stack_list)
    return stack_list
        # return stack_list


def main():
    # f = open('input.txt')
    # contents = f.readlines()
    # f.close()

    contents = sys.stdin.readlines()

    # to obtain the list of tokens
    token_list = [i.rstrip('\n') for i in contents[0].split(' ')]
    # print('list of tokens: ', token_list)

    result = reverse_polish_notation(token_list)

    # print('The result is ', result[0])

    if result == 'TYPE ERROR':
        print('TYPE ERROR')
    elif result == 'SYNTAX ERROR':
        print('SYNTAX ERROR')
    else:
        if len(result) != 1:
            print('SYNTAX ERROR')
        elif result[0] == True:
            print('true')
        elif result[0] == False:
            print('false')
        else:
            print(result[0])


if __name__ == '__main__':
    main()

