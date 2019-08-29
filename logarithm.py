import math
def logFunc(x=10):
    '''
    this function calculates log of an integer
    :param x: integer
    :return: logarithmeic value of integer
    '''
    if x <  0:
         print ("X is not a integer")
    else :
          return math.log(x)

if __name__ == '__main__':
    x = int(input("enter a number"))
    log = logFunc(x)
    print (log)