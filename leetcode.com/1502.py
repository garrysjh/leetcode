## a sequence of numbers is called an arithmetic progression, if the difference between any two consecutive elements is the same
# given an array of numbers arr, return true if the array cna be rearranged to form an arithmetic progrssion, otherwise return false.

def arithmeticProgression(arr: list):
    arithmetic = True
    arr.sort()
    difference = arr[1] - arr[0]
    for element in range(0, len(arr)-1):
        if arr[element+1] - arr[element] != difference:
            arithmetic = False
            break
    return arithmetic

arr = [2,4,7]
print(arithmeticProgression(arr))
        


