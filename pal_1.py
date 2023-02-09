import sys
sys.stdin = open('pal_1.txt')

T = 10
for case in range(1, 11):
    N = int(input())
    arr =[]
    for _ in range(8):
        arr.append(input())

    cnt = 0
    for i in range(8):
        for j in range(8):
            if arr[i][j:j+N] == arr[i][j:j+N][::-1] and len(arr[i][j:j+N]) == N:
                cnt += 1

    for x in range(8):
        row = ''
        for y in range(8):
            row += arr[y][x]
        for k in range(8):
            if row[k:k+N] == row[k:k+N][::-1] and len(row[k:k+N]) == N:
                cnt += 1

    print(f'#{case}', cnt)

