# https://school.programmers.co.kr/learn/courses/30/lessons/77484
def solution(lottos, win_nums):
    answer = []
    unknown_count = 0
    match_count = 0

    for i in range(len(lottos)):
        if lottos[i] == 0:
            unknown_count += 1
            continue
        for j in range(len(win_nums)):
            if lottos[i] == win_nums[j]:
                match_count += 1

    if match_count + unknown_count >= 2:
        answer.append(6 - unknown_count - match_count + 1)
    else:
        answer.append(6)
    if match_count >= 2:
        answer.append(6 - match_count + 1)
    else:
        answer.append(6)

    return answer

