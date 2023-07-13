#moveZeroes
#given an integer array nums, move all 0s to the end of it while maintaining the relative order of the non-zero elements

def moveZeroes(nums: list)->list:
    zeroes = 0
    for element in nums:
        if (element==0):
            zeroes+=1
            nums.remove(0)
    for i in range(0,zeroes):
        nums.append(0)
    return nums

print(moveZeroes([1,0,2,3,4,0,0]))