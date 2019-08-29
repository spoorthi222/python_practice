def sumavg(list,n ):
    '''
     this function finds sum and avg of elements in array
    :param list: array
    :param n: number of elements in list
    :return: sum and avg of elements in array
    '''
    sum=0
    for i in range(n):
        sum = sum+list[i]
    avg = sum / n
    return (avg,sum)


if __name__ == '__main__':

    list = [1,2,3,4,5]
    avg, sum = sumavg(list,5)
    print "sum is ",sum
    print "avg is",avg