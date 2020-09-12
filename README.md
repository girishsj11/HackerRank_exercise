# HackerRank_exercise

## ***Program_1.py***

  **Task**
    
   Given an integer n, perform the following conditional actions:

- If n is odd, print Weird
- If n is even and in the inclusive range of 2 to 5 , print Not Weird
- If n is even and in the inclusive range of 6 to 20, print Weird
- If n is even and greater than 20, print Not Weird

>Input Format

A single line containing a positive integer,n.

>Constraints

n should be in 1 to 100

>Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.


## ***Program_2.py***

  **Task**
  
  The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

- The first line contains the sum of the two numbers.
- The second line contains the difference of the two numbers (first - second).
- The third line contains the product of the two numbers.

>Input Format

The first line contains the first integer,a.
The second line contains the second integer,b.

>Constraints

a & b should be in 1 to 10^10

>Output Format

print three lines as explained above.


## ***Program_3.py***

  **Task**
  
  The provided code stub reads and integer,n, from STDIN. For all non-negative integers i<n, print i^2 .
  
>Example

    n=3
    The list of non-negative integers that are less than n=3  is [0,1,2] . 
    Print the square of each number on a separate line.
    0
    1
    4
       
>Input Format

The first and only line contains the integer,n.

>Constraints

n should be in range of 1 to 21.

>Output Format

Print n lines, one corresponding to each i.




## ***Program_4.py***

  **Task**
  
  An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:
- The year can be evenly divided by 4, is a leap year, unless:
  - The year can be evenly divided by 100, it is NOT a leap year, unless:
    - The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.

>Input Format

Read year, the year to test

>Constraints

Year should be between 1990 to 10^5.

>Output Format

The function must return a Boolean value (True/False). Output is handled by the provided code stub.
