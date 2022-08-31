# https://www.acmicpc.net/problem/1157
# 문제 : 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.
# 출력 : 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
def word_study(word):
    alphabet_dict = dict()
    word = word.lower()

    for i in range(len(word)):
        if word[i] in alphabet_dict:
            alphabet_dict[word[i]] += alphabet_dict[word[i]]
        else:
            alphabet_dict[word[i]] = 1

    alphabet_dict = sorted(alphabet_dict.items(), key=lambda item: item[1], reverse=True)

    if len(alphabet_dict) > 1 and alphabet_dict[0][1] == alphabet_dict[1][1]:
        print("?")
    else:
        print(alphabet_dict[0][0].upper())


word_study(input())
