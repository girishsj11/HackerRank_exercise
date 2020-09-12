# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 19:59:37 2020

@author: giri
"""


'''

Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20 , print Not Weird


1>=n<=100
'''

if __name__ == "__main__":
    num = int(input("Enter the number : "))
    if(num in range(1,101)):
        if(num%2==1):
            print("Weird")
        else:
            if(num in range(6,21)):
                print("Weird")
            else:
                print("Not Weird")
    else:
        print("Entered value is either less than 1 or greater than 100, so please re-try")
