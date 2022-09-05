# https://www.acmicpc.net/problem/4344
# 입력 : 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,
# 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
# 출력 : 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
def above_average(test_case_str):
    student_num = test_case_str.split(' ')[0]
    test_case_str = test_case_str[len(student_num)+1:]
    student_score = list(map(int, test_case_str.split(' ')))

    ave = sum(student_score) / len(student_score)

    count = 0
    for i in range(len(student_score)):
        if int(student_score[i]) > ave:
            count += 1

    print("%.3f%%" % (round(count / len(student_score) * 100, 3)))


test_case_num = int(input())
for i in range(test_case_num):
    above_average(input())