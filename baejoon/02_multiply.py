# https://www.acmicpc.net/problem/2588 (세 자리 수) × (세 자리 수)  
def multiply(a, b):
    sum = 0
    for i in reversed(range(len(b))):
        print(a * int(b[i]))
        sum += a * int(b[i]) * (10 ** (len(b) - i - 1))
    print(sum)


a = int(input())
b = input()
multiply(a, b)
