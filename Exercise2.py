#! /usr/bin/env python3
# Author: Steven Bennett A00987431 Set B ACIT1515
# Date: 2021/11/19 
"""Read contents of text file
ask user to ender a letter
count words in the file that start with a letter
"""

# Imports: any module imports should come immediately following the module docstring

# Global Variables with type annotation


def readWords(file):
    """
(a) Refactor your program to read the file with the readlines() command. 
The program must use a with block to open the file. 
This refactoring should only affect the function that reads the file. 
Use a list comprehension in your function to remove any trailing newline characters from the words.
    """
    with open(file, 'r') as word_file:
        words = word_file.readlines()
        wordlist = []
        for word in words:
            word = word.replace('\n', '')
            wordlist.append(word)
        word_file.close()
    return wordlist

def requestName():
    """
The function prompts for a name. 
It returns the name as well as a list of all words containing the name. 
Matches  are case-insensitive.
    """
    check = input("Enter a name: ")
    i = 0
    while i < len(check): 
        if check[i].isalpha() == False:
            check = input("Enter a real name: ")
            i = 0
        else:
            i += 1
    name = check
    return (name)

def countWords( newwords, name ):
    """
(b) Add a new function has the list of words as a parameter. 
    """
    num = 0
    namein = []
    for word in newwords:
        if name.lower() in word.lower():
            num += 1
            namein.append(word)
    return num, namein

def main():
    """
(c) Update main to display output as shown below.
    """
    file = 'new_words.txt'
    wordlist = readWords(file)
    total = len(wordlist)
    name = requestName()
    num, namein = countWords( wordlist, name )
    print(f'there are {num} words that contain the name {name}')
    print(f'and the first three of them are {namein[0]} {namein[1]} {namein[2]}')
    return num

if __name__ == "__main__":
    main()
