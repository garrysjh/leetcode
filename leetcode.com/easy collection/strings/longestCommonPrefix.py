#longestCommonPrefix
#Write a function to find the longest common prefix string amontst an array of strings, if there is no
#common prefix, return an empty string ""

def longestCommonPrefix(strs: list)->str:
    #assume longest prefix is max of shortest string
    #find the shortest string
    minStr = strs[0]
    for element in strs:
        if len(element)<len(minStr):
            minStr = element
    minLength = len(minStr)

    #check prefix by scaling down from the shortest string
    while (minLength!=0):
        default = False
        prefix = extractPrefixFromWordAndLength(strs[0], minLength)
        for element in strs:
            if(extractPrefixFromWordAndLength(element, minLength) == prefix):
                default = True
            else:
                default = False
        if(default == True):
            return prefix
        minLength-=1
    return ''

        
def extractPrefixFromWordAndLength(string: str, length: int)->str:
    stringArr = [*string]
    newArr = []
    for i in range(0, length):
        newArr.append(stringArr[i])
    return ''.join(newArr)

print(longestCommonPrefix(['tar','f','w']))
