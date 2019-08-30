class calculation:
    '''
    this is a class in which we have implemented a simple calculator
    '''
    def __init__(self, c=0, d=0):
        '''
        this a constructor used to initialise class variables a and b
        '''
        self.a = c
        self.b = d

    def sum(self, c=0, d=0):
        '''
        this function adds two integers if integers are not passed class variables values are considered to add
        '''
        if c==0 & d==0:
            add = self.a+self.b
        else:
            add = c + d
        print "sum is ", add

    def mul(self, c=0, d=0):
        if c==0 & d==0:
            mul = self.a+self.b
        else:
             mul = a * b
        print "multiplication is ", mul

    def sub(self, c=0, d=0):
        if c < d:
            print "error"
        else:
            if c==0 & d==0:
                sub = c-b
            else:
                sub = a - b
            print "substraction is ", sub


if __name__ == '__main__':
    a = int(input("enter a number"))
    b = int(input("enter another number"))
    obj = calculation(5, 6)
    obj.sum(a,b)
    obj.mul(a, b)
    obj.sub(a, b)
