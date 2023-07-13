#given an integer array nums, rotate the array to the right by k steps where k is non-negative

def rotateArray(nums: list, k: int)-> list:
    toAppend = []
    for i in range(0, k):
        toAppend.append(nums.pop())
    for element in nums:
        toAppend.append(element)
    return toAppend

print(rotateArray([1,2,3,4], 2))