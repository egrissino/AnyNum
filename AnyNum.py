## Evan Grissino
## 09/08/15
## Python 3.x only
##
## This program takes any number (n) of any length and itterates it through
## an algorithm to arrive at the number (123).
##
## the algorithm is as follows:
## 1) count the number of even digits in the number, assign to (e)
## 2) count the number of odd digits in the number, assign to (o)
## 3) count the total number of digits in the number, assign to (l)
## create a new number by concatenating (e), (o), and (l)
## this is the new number
## repeat this process with the new number

# Imports
import time

# Global assignments
p = print

## Header
p("Welcome to the 'Any Number To 123' program!")
p("")

# Main loop
while(True):

    ## Prompt for number and assign to (n)
    #Make sure it is a valid number, or quit the program
    try:
        p("Please enter any number or q to quit")
        n = input("::")

        # Check to see if the user is trying to quit
        if n == 'q':
            # break out of mainloop, ending the program
            break

        # Assertion
        n = int(n)
    except:
        # User entered a non numeric value
        print("That is not a valid number for this program!\n")
        # continue to next loop skipping the rest of the loop
        continue
    

    p("")
    p("The number you have entered is: ", n)
    p("")

    ##=======================================
    ## Setup algorithm function
    def NumAlgorithm(n):
        n = str(n)                      # set n to a string so algothithm can handle
        e = 0                           # set even digits equal to zero
        o = 0                           # set odd digits equal to zero 
        l = len(n)                      # create variable l for length of number
        numArray = [0] * l              # create empty array length of number
    
        for a in range(l):              # create array with each value a digit from the number
            numArray[a] = int(n[a])
        
        for a in range(l):              # Find number of even and odd digits
            evenOdd = numArray[a] % 2   # for each element of numArray, set evenOdd as the remainder when divied by two
            if(evenOdd == 0):           # if element is even, evenOdd = 0; if element is odd, evenOdd = 1
                e += 1                  # if evenOdd = 0, increase e by 1
            else:
                o += 1                  # if evenOdd = 1, increase o by
    
        n = str(e) + str(o) + str(l)    #concatenate e, o, and l into new number
        result = [n, e, o, l]           # output result as array    
        return result

    ## Call Algorithm Function

    count = 1                           # set count equal to zero
    a = (n != "123")                    # test if n = 123

    while(a):                           # while n does not equal 123 run algoithm on n
    
        p("Permutation of Algorithm: ", count) # display count number
        p("Old number: ", str(n).rjust(11))
    
        result = NumAlgorithm(n)        # run algorithm on number
        n = result[0]                   # assign the vaiables to the elements of result array
        e = result[1]
        o = result[2]
        l = result[3]
        
        p("Even Digits: ", str(e).rjust(10))           # print even digits
        p("Odd Digits: ", str(o).rjust(11))            # print odd digits
        p("Length: ", str(l).rjust(15))                # print length
        p("New number: ", str(n).rjust(11))            # print number
        p("")
    
    
        a = (n != "123")                # test if number is 123                     
        count += 1                      # increase count by 1
