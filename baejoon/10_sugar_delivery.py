# https://www.acmicpc.net/problem/2839
# 문제 : 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 존재, 더 적은 개수의 봉지를 배달할 수 있도록
# 출력 : 배달하는 봉지의 최소 개수를 출력, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력
def sugar_delivery(weight):
    sugar_5kg = weight // 5
    sugar_3kg = (weight - sugar_5kg * 5) // 3
    while sugar_5kg >= 0 and sugar_3kg <= weight // 3:
        if 5 * sugar_5kg + 3 * sugar_3kg == weight:
            return sugar_5kg + sugar_3kg
        else:
            sugar_5kg -= 1
            sugar_3kg = (weight - sugar_5kg * 5) // 3

    return -1


print(sugar_delivery(int(input())))
