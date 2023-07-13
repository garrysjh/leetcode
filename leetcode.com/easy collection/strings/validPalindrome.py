#validPalindrome
#given a string s, return ture if it is plaindrome, false otherwise

def validPalindrome(s: str)-> bool:
    strArr = [*s]
    left = []
    right = []
    if (len(s)%2==0): #even
        for i in range(int(len(s)/2)-1,-1,-1):
            left.append(strArr[i])
        for i in range(int(len(s)/2), len(s), 1):
            right.append(strArr[i])
            if left == right:
                return True
    elif (len(s)%2!=0): #odd
        for i in range(int(len(s)/2)-1,-1,-1):
            left.append(strArr[i])
        for i in range(int(len(s)/2)+1, len(s),1):
            right.append(strArr[i])
            if left == right:
                return True
    return False

print(validPalindrome('abffba'))