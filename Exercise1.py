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
Read the contents of the file using the open() and read() command.
Your function has one parameter, the name of the file, and returns a list containg the contnets of the file where each item in the list is one word.
    """
    word_file = open(file, 'r')
    content = word_file.read()
    newwords = content.split('\n')
    word_file.close()
    return (newwords)

def requestLetter():
    """
aks the user to enter a single letter.
This funciotn has no parameters.
promts for a letter, which is returne dto the user.
If the user enters anything other than a-z A-Z the function displays an informtative message nd re-prompts until an invalid letter is entered.
    """
    check = input("Enter a letter from a-z or A-Z: ")[0]
    while check.isalpha() == False:
        check = input("Enter a letter from a-z or A-Z: ")[0]
    letter = check
    return (letter)

def example_function():
    """
valide athat something is a letter from a-z or A_Z. 
Takes a string as a parameter and returns true or false
    """
    return 

def countWords( newwords, letter ) -> int:
    """
Count the number of words that satrt with a specified letter.
should not be case sensitive.
Has two parameters
    """
    num = 0
    for word in newwords:
        for firstchar in word:
            if word[0] == letter:
                num += 1

    return(num)

def exone():
    """The 'core' instructions of you program
    
    These are the instructions executed when your program is loaded by the python
    interpreter.

    If you module is imported into another program these will not be run
    """
    file = 'new_words.txt'
    read = readWords(file)
    total = len(read)
    letter = requestLetter()
    num = countWords( read, letter)
    print(f'File {file} contains {total} words.')
    print(f"There are {num} words that start with the letter {letter}")
    return num

# Check if this is being run as a script/program or imported as a module
# If module is loaded by the python interpreter (as opposed to being imported)
# __name__ will equal "__main__"
if __name__ == "__main__":
    exone()
