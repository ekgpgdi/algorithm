# https://www.acmicpc.net/problem/1316 
def group_word_check(word):
    alphabet = [0] * 26
    alphabet[ord(word[0]) - ord('a')] = 1

    for i in range(1, len(word)):
        if word[i] != word[i - 1]:
            index = ord(word[i]) - ord('a')
            if alphabet[index] == 1:
                return 0
            alphabet[index] = 1

    return 1


size = int(input())
count = 0
for i in range(size):
    count += group_word_check(input())

print(count)
