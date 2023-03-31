'''
i: 직원 번호 (idx)
ans = n * 10000
dfs(i, sm)
    if i == n:
        if sm >= b:
            ans = min(ans, sm-b)
    return
'''
def dfs(i, sm):
    global ans

    # if ans <= sm - b:
    #     return
    if ans == 0:
        return

    if i == n:
        if sm >= b:
            ans = min(ans, sm - b)
        return
    
    dfs(i + 1, sm + lst[i])
    dfs(i + 1, sm)

t = int(input())
for case in range(1, t+1):
    n, b = map(int, input().split())
    lst = list(map(int, input().split()))

    ans = n * 10000
    dfs(0, 0)
    
    print(f'#{case}', ans)