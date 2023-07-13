#Given an array of string strs, group the anagrams together. u can return the answer in any rder.
def groupAnagrams(strs: list):
    output = []
    storage = []
    for str in strs:
        a = [*str]
        a.sort()
        a = ''.join(a)
        if a in storage:
            strs.remove(str)
            output.append(str)
        storage.append(a)
    print(output)

groupAnagrams(["eat","tea","tan","ate","nat","bat"])            

