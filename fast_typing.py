import sys
sys.stdin = open('ft.txt')

T = int(input())
for case in range(1, T+1):
    A, B = map(str, input().split())
    m = len(B)
    for i in range(len(A)):
        if A[i:i+m] == B:
            new_A = A.replace(B, '*')
    print(f'#{case}', len(new_A))