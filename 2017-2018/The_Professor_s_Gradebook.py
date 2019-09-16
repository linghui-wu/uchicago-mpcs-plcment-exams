import sys
import math


def main():
    contents = sys.stdin.readlines()

    student_num = int(contents[0].split(' ')[0])
    assignment_num = int(contents[0].split(' ')[1].rstrip('\n'))


    # obtain the student name list
    stu_name_list = []

    for i in contents[1:]:
        stu_name = i.split(' ')[0]
        stu_name_list.append(stu_name)


    # obtain the S_total list
    student_total_grade_list = []
    for indiv in range(student_num):

        assign_grade_list = []

        for grade in contents[indiv + 1].split(' ')[1:-1]:
            assign_grade_list.append(int(grade))


        total_assign_grade = sum(assign_grade_list) - min(assign_grade_list)
        exam_grade = int(contents[indiv + 1].split(' ')[-1])
        total_grade = total_assign_grade + exam_grade

        student_total_grade_list.append(total_grade)


    # obtain the S_grade list
    student_grade_list = []
    max_score = max(student_total_grade_list)


    for i in student_total_grade_list:
        i /= max_score
        i *= 100
        student_grade_list.append(math.ceil(i))


    # obtain the letter grade list
    letter_grade_list = []
    for i in student_grade_list:
        if 90 <= i <= 100:
            letter_grade_list.append('A')
        elif 80 <= i < 90:
            letter_grade_list.append('B')
        elif 70 <= i < 80:
            letter_grade_list.append('C')
        elif 60 <= i <70:
            letter_grade_list.append('D')
        else:
            letter_grade_list.append('F')

    for i in range(student_num):
        print(stu_name_list[i], student_total_grade_list[i], student_grade_list[i], letter_grade_list[i])


if __name__ == '__main__':
    main()

