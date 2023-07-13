#Two Sum
#Given an array of integers nums and an integer target, return indices of the two numbers
#such that they add up to target

def twoSum(nums: list, target: int) -> list:
    result = []
    for i in range(0, len(nums), 1):
        for j in range(0, len(nums), 1):
            if(i!=j):
                if(nums[i] + nums[j] == target):
                    result.append(i)
                    result.append(j)
                    return result

nums = [3,2,4]
target = 6
print(twoSum(nums, target))