#Given two strings ransomNote and magazine, return true if ransomNote can be constructed using the letters from magazine and false
#otherwise
#each letter can only be used once

def ransomNote(ransomNote: str, magazine: str) -> bool:
    ransomArr = [*ransomNote]
    magazineArr = [*magazine]
    for element in magazineArr:
        if element in ransomArr:
            ransomArr.remove(element)
    if ransomArr == []:
        return True
    else:
        return False

print(ransomNote('aa', 'aab'))
