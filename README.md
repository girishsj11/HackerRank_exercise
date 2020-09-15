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

Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

>Input Format

Read year, the year to test

>Constraints

Year should be between 1990 to 10^5.

>Output Format

The function must return a Boolean value (True/False). Output is handled by the provided code stub.


## ***Program_5.py***

  **Task**
  
  The included code stub will read an integer,n, from STDIN. Without using any string methods, try to print the following:
  
  123....n
  
  Note that "...." represents the consecutive values in between.
  
>Example

     n=5
     print the string 12345.
     
>Input Format

The first line contains an integer n.

>Constraints

n should be between 1 to 150.

>Output Format

Print the list of integers from 1 through n as a string, without spaces.



## ***Program_6.py***

  **Task**
  
  Consider that vowels in the alphabet are a, e, i, o, u and y.
  Function score_words takes a list of lowercase words as an argument and returns a score as follows:
  
    The score of a single word is 2 if the word contains an even number of vowels. Otherwise, the score of this word is 1. 
    The score for the whole list of words is the sum of scores of all words in the list.
  
>Input Format

The input is read by the provided locked code template. In the first line, there is a single integer n denoting the number of words. In the second line, there are n space-separated lowercase words.

>Constraints

- n should be in 1 to 20 .
- Each word has at most 20 letters and all letters are English lowercase letters.

>Output Format

It calls function score_words with the list of words read from the input as the argument and prints the returned score to the output.
        
>Examples 

       Sample Input 0                    
       2                                 
       hacker book
       
       Sample Output 0
       4
       
       Explanation 0 
            There are two words in the input: hacker and book. 
            The score of the word hacker is 2 because it contains an even number of vowels, i.e. 2 vowels, 
            and the score of book is 2 for the same reason. Thus the total score is 2+2=4.
                   
                   
                   
       Sample Input 1                    
       3                                
       programming is awesome 
       
       Sample Output 1
       4
       
       Explanation 1 
            There are 3 words in the input: programming, is and awesome. 
            The score of programming is 1 since it contains 3 vowels, an odd number of vowels. 
            The score of is is also 1 because it has an odd number of vowels. 
            The score of awesome is 2 since it contains 4 vowels, an even number of vowels. Thus, the total score is 1+1+2=4 .
                   
                   
      
       
       
       
       
