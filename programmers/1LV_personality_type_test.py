# https://school.programmers.co.kr/learn/courses/30/lessons/118666
def solution(survey, choices):
    answer = ''
    score = dict(R=0, T=0, C=0, F=0, J=0, M=0, A=0, N=0)
    for i in range(len(survey)):
        if choices[i] > 4:
            score[survey[i][:1]] += 4 - choices[i]
        elif choices[i] < 4:
            score[survey[i][1:]] += choices[i] - 4

    print(score)

    answer += 'R' if score['R'] >= score['T'] else 'T'
    answer += 'C' if score['C'] >= score['F'] else 'F'
    answer += 'J' if score['J'] >= score['M'] else 'M'
    answer += 'A' if score['A'] >= score['N'] else 'N'

    print(answer)


solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])
