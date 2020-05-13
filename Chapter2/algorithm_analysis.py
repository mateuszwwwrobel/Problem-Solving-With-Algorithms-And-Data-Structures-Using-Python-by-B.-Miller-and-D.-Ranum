import time

def sumOfN2(n):
   start = time.time()

   theSum = 0
   for i in range(1,n+1):
      theSum = theSum + i

   end = time.time()

   return theSum,end-start



#print("Sum is %d required %10.7f seconds"%sumOfN2(1000000021))




def sumOfN3(n):

    start = time.time()
    x = (n*(n+1))/2
    end = time.time()
    return x, end-start


print("Sum is %d required %10.7f seconds"%sumOfN3(100000001))