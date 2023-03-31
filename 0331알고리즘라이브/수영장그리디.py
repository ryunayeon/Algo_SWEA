t = int(input())
for case in range(1, t+1):
    day, mon, three_mon, year = map(int, input().split())
    lst = [0] + list(map(int, input().split()))

    s = [0] * 13
    for i in range(1, 13):
        # 가능한 방법 중 i달 까지의 최소 비용
        s[i] = s[i-1] * day * lst[i]
        s[i] = min(s[i], s[i-1] + mon)
        if i >= 3:
            s[i] = min(s[i], s[i-3] + three_mon)
        if i >= 12:
            s[i] = min(s[i], s[i-12] + year)

    ans = s[12]

    print(f'#{case}', ans)