def divisors():
    '''
    this function prints all the divisors of a number
    :return:
    '''
    num = int(input("enter a number"))
    list = []
    for i in range(2,num):
       if(num % i == 0):
            list.append(i)
    print list

if __name__ == '__main__':
    divisors()

