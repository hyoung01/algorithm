a= [0,0,0]

a[0], a[1], a[2] = map(int, input().split())
p =0

a.sort()

if a[0]==a[1] and a[1]==a[2] :
    p = 10000+a[0]*1000
elif a[0]!=a[1] and a[1]!=a[2] and a[0]!=a[2]:
    p = a[2]*100
else:
    if a[0] == a[1]:
        p = 1000+a[0]*100
    elif a[1] == a[2]:
        p = 1000+a[1]*100
    else:
        p = 1000+a[2]*100

print(p)