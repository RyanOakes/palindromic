#Palindrome Detector

##Synopsis

This program exists to test whether or not a user-created string qualifies as a
palindrome. A palindrome is a word or phrase that, when reversed, reads the exact
same as forwards, e.g. racecar.

##Programming Objectives

1. Understand how to manipulate strings
2. Understand how strings are related to lists
3. Understand recursion
4. Be able to strip characters out of strings
5. Be able to change the case of strings
6. Be able to look at substrings
7. Be able to add, commit, and push to GitHub

##Requirements

Write a program that, when run, asks the user to input some text. It can be a phrase, a sentence, or multiple sentences. After it is entered, your program will let the user know if it is a palindrome or not by printing "is a palindrome" or "is not a palindrome" in the output.

Letter casing and punctuation do not matter when testing a palindrome. All of the following are valid palindromes:

1. stunt nuts
2. Lisa Bonet ate no basil.
3. A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal: Panama!
4. Doc, note, I dissent. A fast never prevents a fatness. I diet on cod.

Write your main() function to ask the user for a word/sentence, pass it into the is_palindrome function, and state whether or not the the sentence is palindromic.
Write your is_palindrome function using recursion.


Your program must pass all of the tests provided in palindrome_test.py. You should be able to run this with python palindrome_test.py.


You need a function named is_palindrome that takes a string and returns a boolean (True or False). Your program must use this function.
