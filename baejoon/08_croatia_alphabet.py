# https://www.acmicpc.net/problem/2941
# 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력 
def croatia_alphabet(word):
    change_word = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    start_word = ["c", "d", "l", "n", "s", "z"]
    count = 0
    i = 0

    while i < len(word):
        if word[i] in start_word:
            if word[i:i + 2] in change_word:
                i += 1
            elif word[i: i + 3] in change_word:
                i += 2
            count += 1
        else:
            count += 1
        i += 1

    return count


print(croatia_alphabet(input()))
