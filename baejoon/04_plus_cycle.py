# https://www.acmicpc.net/problem/1110
# 입력 : 첫째 줄에 N이 주어진다. N은 0보다 크거나 같고, 99보다 작거나 같은 정수이다.
# 출력 : 첫째 줄에 N의 사이클 길이를 출력한다.
def plus_cycle(num):
    a = num // 10  # 2
    b = num % 10  # 6
    count = 0
    new_number = str(a + b)  # 8
    while True:
        count += 1
        new_number = str(b) + str(int(new_number) % 10)  # 68
        if int(new_number) == num:
            break
        b = int(int(new_number) % 10)
        new_number = int(new_number) // 10 + int(new_number) % 10
    print(count)


num = int(input())
plus_cycle(num)
