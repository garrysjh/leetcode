#Missing Number
#Given array nums containg n distinct numbers in range [0,n], return only number in range that is missing

def missingNumber(nums: list)->int:
    #sort
    nums.sort()
    for i in range(0,nums[len(nums)-1]):
        if (i!=nums[i]):
            return i

print(missingNumber([0,1]))