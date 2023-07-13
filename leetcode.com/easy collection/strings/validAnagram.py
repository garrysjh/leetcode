#validAnagram
#given 2 strings s and t, return true if t is an anagram of s and false otherwise

def validAnagram(s: list, t: list)->bool:
    return (set(s)==set(t))

print(validAnagram('ant','tan'))