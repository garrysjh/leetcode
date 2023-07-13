#longest palindromic substring
#given string s, return longest palindromic substring in s
def returnSubstring(s: str, low: int, high: int)-> str:
    strArr = [*s]
    newStr = []
    for i in range(low, high+1):
        newStr.append(strArr[i])
    return ''.join(newStr)

def checkPalindrome(s: str)-> bool:
    output = False
    strArr = [*s]
    left = []
    right = []
    if (len(strArr)%2==0): #even
        for element in range(int(len(strArr)/2)-1,-1, -1):
            left.append(strArr[element])
        for element in range(int(len(strArr)/2), len(strArr), 1):
            right.append(strArr[element])            
        if (left == right):
            output = True
    if (len(strArr)%2!=0): #odd
        for element in range(int(len(strArr)/2)-1,-1,-1):
            left.append(strArr[element])
        for element in range(int(len(strArr)/2)+1,len(strArr),1):
            right.append(strArr[element])
        if (left==right):
            output = True
    return output

def longestPalindromicSubstring(s: str)->  str:
    width = len(s)
    low=0
    high=low+width-1
    if(checkPalindrome(returnSubstring(s,low,len(s)-1))):
            return returnSubstring(s,low,len(s)-1)
    while (width!=0):
        width-=1
        low=0
        high=low+width-1
        while(high<len(s)):
            low+=1
            high=low+width-1
            if (high>=len(s)):
                break
            if(checkPalindrome(returnSubstring(s,low,high))):
                return returnSubstring(s,low,high)
        
print(longestPalindromicSubstring('ccd'))






