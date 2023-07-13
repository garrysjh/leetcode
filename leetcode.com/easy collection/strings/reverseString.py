#reverseString
#write a function that reverses a string

def reverseString(s: list)-> list:
    reversed = []
    for i in range(len(s)-1,-1,-1):
        reversed.append(s[i])
    return reversed

print(reverseString(['a','b','c']))