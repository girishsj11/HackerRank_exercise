# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 22:16:55 2020

@author: giri
"""
'''
Print the list of integers from 1 through n as a string, without spaces.
'''



if __name__ == '__main__':
    num = int(input("Enter number : "))
    for i in range(1,num+1):
        print(i,end="")
