'''
Date: Feb 02
Challenge: Check if the given two strings are Anagram
'''

s1 = input(f'Provide me the first string: ')
s2 = input(f'Provide me the second string: ')

if(sorted(s1) == sorted(s2)):
    print('Given strings are Anagrams')
else:
    print('Given strings are not an Anagrams')
