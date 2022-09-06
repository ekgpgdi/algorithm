# https://www.acmicpc.net/problem/1011
# 문제 : Kn = Kn-1 -1 or Kn-1 or Kn-1 +1
# y지점에 도착하기 바로 직전의 이동거리는 반드시 1
# x지점부터 정확히 y지점으로 이동하는데 필요한 공간 이동 장치 작동 횟수의 최솟값
def fly_me_to_the_alpha_centauri(x, y):
    count = 0
    pre_distance = 0
    mid = (y + abs(x)) // 2
    start_x = x

    while x <= mid:
        pre_distance += 1
        x += pre_distance
        if x <= mid:
            count += 1

    sum = 0
    for i in range(count):
        sum += i
    sum += count

    count *= 2
    if x - pre_distance + sum != y:
        count += 1

    if start_x + sum + pre_distance < y - sum:
        count += 1

    print(count)


test_case = int(input())
for i in range(test_case):
    input_x, input_y = input().split()
    fly_me_to_the_alpha_centauri(int(input_x), int(input_y))
