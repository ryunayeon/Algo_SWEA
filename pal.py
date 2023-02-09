import sys
sys.stdin = open('pal.txt')

T = int(input())

for case in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for i in range(N):
        arr.append(input())

    # 행에서 회문 검사
    for j in arr:
        for k in range(N-M+1):
            if j == j[::-1] or j[k:k+M] == j[k+M:k-1:-1]:
                print(f'#{case}', j[k:k+M])

    # #열을 행으로 만든 뒤 회문 검사
    for x in range(N):
        nw = ''
        for y in range(N):
            nw += arr[y][x]
        for z in range(N-M+1):
            if nw == nw[::-1] or nw[z:z+M] == nw[z+M:z-1:-1]:
                print(f'#{case}', nw[z:z+M])





