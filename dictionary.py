from collections import defaultdict

n, m = map(int, input().split())

A = defaultdict(list)
for i in range(1, n+1):
    A[input()].append(i)

B = []
for i in range(m):
    B.append(input())

for b in B:
    if b in A:
        print(" ".join(map(str, A[b])))
    else:
        print(-1)
