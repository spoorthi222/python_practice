def sumavg(list,n ):
    sum=0
    for i in range(n):
        sum = sum+list[i]
    avg = sum / n
    return (avg,sum)

list = []
n=int(input("enter  no array elements"))
for i in range(n):
    ele = int(input())
    list.append(ele)
print (list)
avg, sum = sumavg(list,n)
print "sum is ",sum
print "avg is",avg