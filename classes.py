class calculation:
    def __init__(self,c,d):
        self.a = c
        self.b =d


    def sum(self):
         add = self.a+self.b
         print "sum is ",add

    def mul(self,a,b):
        mul = a*b
        print "multiplication is ",mul

    def sub(self,a,b):
        if a < b:
            print "error"
        else:
            sub = a-b
            print "substraction is ",sub


a = int(input("enter a number"))
b = int(input("enter another number"))
obj = calculation(a,b)
obj.sum()
obj.mul(a,b)
obj.sub(a,b)

