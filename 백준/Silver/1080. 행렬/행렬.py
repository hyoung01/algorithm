#1080 행렬
from sys import stdin


def change(a, i, j):
    for p in range(3):
        for q in range(3):
            if a[i+p][j+q] == 0:
                a[i+p][j+q]=1
            else:
                a[i+p][j+q]=0


n, m= map(int, input().split())

a = [list(map(int, stdin.readline().rstrip())) for j in range(n)]
b = [list(map(int, stdin.readline().rstrip())) for j in range(n)]
c=0
for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            change(a, i, j)
            c+=1
for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            c=-1
print(c)