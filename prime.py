
def prime_num():
    '''
    this function finds a given number is prime or not
    :return: nothing
    '''
    num = int(input("enter a number"))
    q = num /6
    r = num % 6
    if num == 6*q +r :
        if (r==1) | (r == 5) :
            print "Prime number"
        else:
            print "Not a prime number"

if __name__ == '__main__':
    prime_num()