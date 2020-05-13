""" counter = 1
done = True
while counter <= 2 and not done:
    print("Lecimy z tematem.")
    counter = counter+1 """

""" for item in [3,3,5,3,7,7]:
    print(item)

print(item)
 """


""" x = -34
print(x)
x=abs(x)
print(x) """

""" sqlist=[]

for x in range(1,16):
    sqlist.append(x*x)

print(sqlist) """

""" sqlist=[x*x for x in range(1,15) if x%2]

print(sqlist) """

""" import math 

anumber = int(input("Please enter a number: "))
try:
    print(math.sqrt(anumber))
except: 
    if anumber < 0:
        print("no my fiend") """

""" def sqrt(n):
    print(n**2)

sqrt(4)
 """

""" def squareroot(n):
    root = n/2
    for k in range(20):
        root = (1/2)*(root+(n/root))

    return print(root)
    
squareroot(4891) """


def gcd(m,n):
    while m%n !=0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n



class Fraction:
    def __init__(self,top,bottom):
        if not isinstance(top, int):
            valErr = ValueError("{} is not integer".format(top))
            raise valErr
        if not isinstance(bottom, int):
            valErr = ValueError("{} is not integer".format(bottom))
            raise valErr

        if top < 0 and bottom < 0:
            top = abs(top)
            bottom = abs(bottom)
        elif bottom < 0:
            top = -top
            bottom = abs(bottom)
        common = gcd(top,bottom)
        self.num = top//common
        self.den = bottom//common

        

    def __str__(self):
        return str(self.num) + "/" + str(self.den)



    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den*otherfraction.den
        return Fraction(newnum,newden)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum


    def __sub__(self, otherfraction):
        newden = self.den * otherfraction.den
        newnum = (self.num * otherfraction.den) - (self.den * otherfraction.num)
        return Fraction(newnum,newden)

    def __mul__(self, otherfraction):
        newden = self.den * otherfraction.den
        newnum = self.num * otherfraction.num
        return Fraction(newnum,newden)

    def __truediv__(self, other):
        newden = self.den*other.num
        newnum = self.num*other.den
        return Fraction(newnum,newden)

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

    def __gt__(self,other):
        firstFraction = self.num/self.den
        secondFraction = other.num/other.den
        if firstFraction > secondFraction:
            return True
        else:
            return False

    def __ge__(self,other):
        firstFraction = self.num/self.den
        secondFraction = other.num/other.den
        if firstFraction >= secondFraction:
            return True
        else:
            return False

    def __lt__(self,other):
        firstFraction = self.num/self.den
        secondFraction = other.num/other.den
        if firstFraction < secondFraction:
            return True
        else:
            return False

    def __le__(self,other):
        firstFraction = self.num/self.den
        secondFraction = other.num/other.den
        if firstFraction <= secondFraction:
            return True
        else:
            return False

    def __ne__(self,other):
        firstFraction = self.num/self.den
        secondFraction = other.num/other.den
        return firstFraction != secondFraction
    
    def __radd__(self, other):
        if other == 0:
            return self
        else:
            other = Fraction(other, 1)
            return self.__add__(other)




f1 = Fraction(-1,6)
f2 = Fraction(0,1)

#f2 = Fraction.get_den(f1)

f3 = f1*f2

print(f3)










