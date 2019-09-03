
def prime_num():
    '''
    this function finds a given number is prime or not
    :return: nothing
    '''
    num = int(input("enter a number"))
    q = num /6
    r = num % 6
    if num == 6*q +r :
        if (r == 5) :
            print "Prime number"
        elif (r==1) :
            for i in range(2,num):
                if num%i == 0 :
                    print "not a prime number "
                    found =1
                    break
            if (found !=1 ):
                 print "prime number"

        else:
            print "Not a prime number"

if __name__ == '__main__':
    prime_num()