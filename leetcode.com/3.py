#given a string s
#find length of longest subtring without repeating characters
#eg abcabcab = abc
#eg bbbbb = b
#eg pwwkew = wke

#basically, each letter must be unique

def unique(arr: list):
    return len(arr) == len(set(arr))

def longestSubtring(s: str):
    strarr = [*str]
    #check if already is longest substring
    if(unique(strarr)):
        return len(strarr)


def longest_non_repeating_substring(string: str):
    i = 0
    j = 0
    ans = 0
    map = {}
    while j < len(string):
        if string[j] not in map or i > map[string[j]]:
            ans = max(ans, j - i + 1)
            map[string[j]] = j
        else:
            i = map[string[j]] + 1
        j += 1
    return ans




print(longest_non_repeating_substring('abcabcbb'))