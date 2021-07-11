inp = list(map(int,input().strip().split(',')))
op = []
for i in inp:
    num = 10**i - 1
    # print(num)
    while(num%i != 0):
        num-=1
    op.append(num)
print(*op,sep=',')  