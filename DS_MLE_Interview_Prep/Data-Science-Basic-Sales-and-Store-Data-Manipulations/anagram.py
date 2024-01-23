
#Counter is lib to count characters of str and return a dict
from collections import Counter


def anagram_checker(a, b):
    #checking anagram via separating characters of the string
    if sorted(a) == sorted(b):
        print("They are anagrams")
    else:
        #find differences from each other via taking the difference of counted dicts
        print('remove ' + str(sum((Counter(a) - Counter(b)).values()))
        + ' characters from ' + f'"{a}"' + ' and ' + 
        str(sum((Counter(b) - Counter(a)).values())) + 
        ' characters from '+ f'"{b}"' )    


first_string = input("Provide the first string: ")
second_string = input("Provide the second string: ")
anagram_checker(first_string, second_string) 
