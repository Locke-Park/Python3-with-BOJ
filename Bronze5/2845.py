a, b = map(int, input().split())
q,w,e,r,t =map(int,input().split())
x = [q,w,e,r,t]
for i in range(5):
    print(x[i]-a*b,end=' ')
