#reverseInteger
#given a 32bit integer x, return x with its digits reversed

def reversed(arr: list)->list:
    reversed = []
    for i in range(len(arr)-1,-1,-1):
        reversed.append(arr[i])
    return reversed

def reverseInteger(x: int)-> int:
    intArr = [*str(x)]
    return ''.join(reversed(intArr))

print(reverseInteger(32))