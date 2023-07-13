#twoSum
#given an array of integers nums and an integer target, return indices of the two such that they add up to target

def twoSum(nums: list, target: int) -> list:
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if (i!=j):
                if(nums[i]+nums[j]==target):
                    return [i,j]
                
print(twoSum([1,2,3,4],4))