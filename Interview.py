import sys
from time import time
# this will find the largest number in an array
def largest (arr):
    # initialize variable for keeping track of the largest integer
    largest = 0
    # if the array is empty, exit
    if(len(arr) == 0):
        print largest
        return
    # go through the entire array, and keep replacing large with i if i is bigger
    for i in arr:
        if i > largest:
            largest = i
    print "\nThe largest number is: ", largest, "\n"

# This is the basic fizzbuzz implementation
def fizzbuzz (n):
    # make sure there are n's to print
    if n < 0 :
        print "Enter a number greater than 0"
        return

    # print number or string
    for x in range (0, n):
        if x%15 == 0 :
            print "FIZZBUZZ"
        elif x%3 == 0 :
            print "FIZZ"
        elif x%5 == 0 :
            print "BUZZ"
        else:
            print x

# this will Bubble Sort an array
def BubbleSort (arr):
    count = 0
    for x in range (0, len(arr)-1):
        if arr[x] > arr[x+1]:
            arr[x], arr[x+1] = arr[x+1], arr[x]
            count += 1
    if count > 1 :
        BubbleSort(arr)

# this is the general fizzbuzz implementation
def generalFizzBuzz (dict, n):

    # Make sure there are n's to print
    if n < 0:
        print "Enter a number greater than 0"
        return

    # Get all keys in dictonary into an array
    arr = []
    for x in dict:
        arr.append(x)

    BubbleSort(arr)

    # print number or string, numbers in dictionary are traversed based on the sorted array
    for x in range (0, n):
        # storage string
        s = ""
        for y in arr:
            # if n is divisible by something in the dictionary, append the dictionary item to s
            if x%y == 0 :
                s += dict[y]
        # when the checks are done, print of s if anything was appended, and x otherwise
        if (s == ""):
            print x
        else:
            print s
    print "\n"
    
#This returns the factorial of a number
def factorial(n):
    if ((n==1)|(n==0)) :
        return 1
    elif(n > 1):
        return n * factorial(n-1)
    else:
        return 0

def fib(n):
    if n < 0:
        print "Enter a number bigger than 1"
        return
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
#largest([1, 2, 3, 4])
#largest([])
#largest([1, 60, 4])

#fizzbuzz(100)
#fizzbuzz(-1)

dict = {9: "Nine", 3: "Three", 7 : "Seven", 2: "Two"}

generalFizzBuzz(dict, 10000)

# this will find what the maximum recursion depth for factorial is.
try:
    for x in range (0, 0):
        print factorial(x)
except:
    print"\n"
    for i in sys.exc_info():
        print i
    print "\nx was: ", x

# this will compute all the recursions up to whatever number specified and give statistics about how long it took
totalTime = time()
try:
    for x in range (0, 1):
        second = time()
        print "\nFib ", x, " is ", fib(x), " and takes " , (time()-second) , " seconds to compute"
    print "\nComputing everything up to fib ", x, " takes ", (time()-totalTime) , " seconds\nWhich is ", ((time()-totalTime)/60) , " minutes."
except:
    print"\n"
    for i in sys.exc_info():
        print i
    print "\nx was: ", x, ". A failure was reached after ", (time()-totalTime), " seconds."