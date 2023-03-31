'''
if n > 12:
    ans = min(ans, sm)
return
dfs(n+1, sm + day * lst[i])
dfs(n+1, sm + mon)
dfs(n+3, sm + 3_mon)
dfs(n+12, sm + year)

<그리디로 풀기>
s[i]
if i >= 3: 분기권 적용

'''
def dfs(i, sm):
    global ans

    if ans <= sm:
        return

    if i > 12:
        ans = min(ans, sm)
        return
    dfs(i + 1, sm + day * lst[i])
    dfs(i + 1, sm + mon)
    dfs(i + 3, sm + three_mon)
    dfs(i + 12, sm + year)



t = int(input())
for case in range(1, t+1):
    day, mon, three_mon, year = map(int, input().split())
    lst = [0] + list(map(int, input().split()))

    ans = 365 * 3000
    dfs(1, 0)

    print(f'#{case}', ans)