#1149 RGB거리

import sys

n = int(input())
a =[]
for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(1, len(a)):
    a[i][0] = min(a[i - 1][1], a[i - 1][2]) + a[i][0]
    a[i][1] = min(a[i - 1][0], a[i - 1][2]) + a[i][1]
    a[i][2] = min(a[i - 1][0], a[i - 1][1]) + a[i][2]
print(min(a[n - 1]))