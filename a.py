n = input()
count = 1
for i in range(len(n)):
    for j in range(i,len(n)-1):
        print(" ",end="")
    print(n[:count])
    count+=1
count = 1
for i in range(len(n)-1,0,-1):
    print(n[count:])
    count+=1