'''
백트래킹: 가능한 모든 경우 -> 답 but, 시간 초과 주의
[1] 재귀 종료조건 설정 (N)
    lst = [1, 2, 1, 2], 이진트리 -> 멀티트리
    n: 숫자 번호(index)
[2] tree(시각적)
[3] ans = 0
    dfs(n, sm,)
    if n == N: -> 종료
        if sm == k:
            ans += 1
            return
    * 포함
    dfs(n+1, sm + lst[i])
    * 포함 x
    dfs(n+1, sm)
'''
def dfs(i, sm):
    global ans
    # [3] 가지치기 -> 가장 마지막에..
    if k < sm:
        return

    # [1] 종료 조건
    if n == i:
        if sm == k:
            ans += 1
        return
    # [2] 하부
    # 포함
    dfs(i+1, sm + lst[i])
    # 불포함
    dfs(i+1, sm)


t = int(input())
for case in range(1, t+1):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))

    ans = 0
    dfs(0, 0)


    print(f'#{case}', ans)