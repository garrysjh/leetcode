#FirstUniqueCharacterInAString
#given string s, find the first non-repeating character in it and return its index, if it does not exist
#return -1

def firstUnique(s: str)-> int:
    strArr = [*s]
    count = {}
    for element in set(strArr):
        count[f'{element}'] = 0
    for element in strArr:
        count[f'{element}'] += 1
    returnable = [i for i in count if count[i]==1]
    return strArr.index(int(returnable[0]))

print(firstUnique([1,2,2,3,3,4,4]))