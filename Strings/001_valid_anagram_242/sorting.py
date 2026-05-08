s = input("Enter first string: ")
t = input("Enter second string: ")

if sorted(s) == sorted(t):
    print("Valid Anagram")
else:
    print("Not Anagram")