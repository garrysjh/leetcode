#Valid Anagram
#given two strings s and t, return true if t is an anagram of s, and false otherwise

#an anagram is a word or phrase formed by rearranging the letters of a different word of phrase typically using the 
#original letters exactly once


def anagram(s, t):
    isAnagram = False
    array = [char for char in s]
    array2 = [char for char in t]
    for i in array:
        if i in array2:
            array2.remove(i)
        if len(array2) == 0:
            isAnagram = True
            break
    print(isAnagram)


anagram("rat", "car")
