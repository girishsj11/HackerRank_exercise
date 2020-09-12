# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 21:13:44 2020

@author: giri
"""

'''
The provided code stub reads and integer, n, from STDIN. For all non-negative integers i<n, print i^2 .

'''

if __name__=="__main__":
    num = int(input("Enter the input number : "))
    for i in range(num):
        print(i*i)
