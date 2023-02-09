import sys
sys.stdin = open('str.txt')

T = int(input())
for case in range(1, T+1):
    str1 = str(input())
    str2 = str(input())

    if str1 in str2:
        print(f'#{case}', 1)
    else:
        print(f'#{case}', 0)