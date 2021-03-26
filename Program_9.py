'''
The good string is a string that contains only vowels , find out the longest length of the good string among the given string.

Example : 
  input - 'abcaaba'
  ouput - 2 (since aa is the good substring among the give string which contains only vowels)

'''

def longest_substring(string):
    res=count=0
    vowels = ['a','e','i','o','u']
    for char in string.lower():
        if(char in vowels):
            count += 1
        else:
            res = max(res,count)
            count = 0
    print(max(res,count))
    
if __name__ == "__main__":
    string = input("Enter your input string here : ")
    longest_substring(string)
