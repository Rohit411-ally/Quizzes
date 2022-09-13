#length of the input list
a = int(input())
#input list
x=list(map(int, input().split()))
#initializing the count
count=0
for i in x:
    y=[]
    for j in range(1,i):
        y.append(j)
    n=len(y)//2
    if i%2==0:
        n+=1
    #creating a list and its reverse to form unique pairs to compare
    z=y[::-1]
    z=z[:n]
    y=y[:n]
    for j in range(n):
        #condition to determine a good number
        if y[j]^z[j]==i and y[j]&z[j]==0:
            count+=1
            break
print(count)