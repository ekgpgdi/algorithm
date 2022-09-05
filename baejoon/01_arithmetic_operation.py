# https://www.acmicpc.net/problem/10869
# 문제 : 두 자연수 a와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.
# 입력 : 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
# 출력 : 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다. 

# 더하기
def plus(a, b):
    return a + b


# 빼기
def minus(a, b):
    return a - b


# 곱하기
def multiply(a, b):
    return a * b


# 나누기
def divide(a, b):
    return int(a / b)


# 나머지
def remainder(a, b):
    return a % b


def arithmetic_operation(a, b):
    print(plus(a, b))
    print(minus(a, b))
    print(multiply(a, b))
    print(divide(a, b))
    print(remainder(a, b))


a, b = input().split()
arithmetic_operation(int(a), int(b))
