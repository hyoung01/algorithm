#1105 팔



l, r= map(int, input().split())

L=str(l)
R = str(r)

if len(L)!= len(R):
    print(0)

else:
    if r-l==99:
        print(1)
    else:
        c=0
        for i in range(len(L)):
            if L[i] == R[i]:
                if L[i] == '8':
                    c += 1
            else:
                break

        print(c)