#1047 z



n, r, c = map(int, input().split())
count = 0
while n != 0:

    n -= 1
    s = 2 ** n

    if r < s and c < s:
        count += 0

    elif r < s and c >= s:
        count += s * s
        c -= s

    elif r >= s and c < s:
        count += s * s * 2
        r -= s

    else:
        count += s * s * 3
        r -= s
        c -= s

print(count)