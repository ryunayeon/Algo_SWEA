def dfs(k, tst, ci, cj):
    if k == 7:
        sset.add(tst)
        return
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs(k + 1, tst * 10 + arr[ni][nj], ni, nj)

t = int(input())
for case in range(1, t+1):
    arr = [list(map(int, input().split())) for _ in range(4)]

    sset = set()
    for i in range(4):
        for j in range(4):
            dfs(1, arr[i][j], i, j)
    
    ans = len(sset)
    print(f'#{case}', ans)