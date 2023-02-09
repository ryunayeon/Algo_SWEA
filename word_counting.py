import sys
sys.stdin = open('word_counting.txt')

T = int(input())
for _ in range(1, T+1):
    str1 = input()
    str2 = input()

    cnt = [0] * len(str1)
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                cnt[i] += 1

    print(f'#{_}', max(cnt))