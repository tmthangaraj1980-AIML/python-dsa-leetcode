from collections import Counter
s = input("Enter first string: ")
t = input("Enter second string: ")

if Counter(s) == Counter(t):
    print("Valid Anagram")
else:
    print("Not Valid Anagram")