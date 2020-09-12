# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 21:57:17 2020

@author: giri
"""


'''

Given a year, determine whether it is a leap year. If it is a leap year, 
return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and 
passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

'''




def is_leap(year):
    leap = False
    
    if(year%4==0):
        if(year%100==0 and year%400==1):
            return leap
        else:
            leap = True
    
    return leap


if __name__ == "__main__":
    year =  int(input("Enter the year to check whether its leap year or not : "))
    print(is_leap(year))
