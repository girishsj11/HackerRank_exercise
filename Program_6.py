# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 21:00:28 2020

@author: giri
"""

def score_words(word,vowels):
    score = 0
    word_list_without_spaces = (word.strip(' ')).split(' ')
    
    for bunch_of_words in word_list_without_spaces:
        vowel_count = 0
        
        for char in bunch_of_words:
            if char in vowels:
                vowel_count+=1
            else:
                continue
        if(vowel_count>0):
            if (vowel_count%2==0):
                score+=2
            else:
                score+=1
        else:
            continue
    return score
        


if __name__ == "__main__":
    vowels = ['a','e','i','o','u','y']
    word_count = int(input("Enter the number of words to be present on user input string : "))
    word = str(input("Enter the word to get the vowel score of it : "))
    if(len((word.strip(' ')).split(' '))==word_count):
        print(" \nVowel score of input string '{}' is '{}' ".format(word,score_words(word, vowels)))
    else:
        print("\nEntered count & word length is not matching ! ")
