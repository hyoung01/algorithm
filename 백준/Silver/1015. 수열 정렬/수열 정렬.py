n = int(input())
a = list(map(int, input().split()))

l = sorted(a)
b = []
for i in range(n):
    for j in range(n):
        if a[i] == l[j]:
            if j not in b:
                b.append(j)
                break

for i in range(n):
    print(b[i], end= ' ')
