s = input("Enter first string: ")
t = input("Enter second string: ")

if len(s) != len(t):
    print("Not Anagram")
else:

    countS = {}
    countT = {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    if countS == countT:
            print("Valid Anagram")
    else:
            print("Not Anagram")