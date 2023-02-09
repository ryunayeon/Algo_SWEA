import sys
sys.stdin = open("gns.txt")

numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())
for _ in range(1, T+1):
    case, N = input().split()
    arr = input().split()
    # print(arr)

    cnt = [0] * 10
    for i in range(10):
        for j in arr:
            if j == numbers[i]:
                cnt[i] += 1

    print(case)
    for k in range(10):
        for l in range(cnt[k]):
            print(numbers[k], end=' ')
    print()