# neetcode
# given an integer array nums, return true if any value appears at least twice in the array, and return false if
# every element is distinct
def containsDuplicate(nums):
    containsDupe = False
    for i in nums:
        if (nums.count(i))>1:
            containsDupe = True
            break
    print(containsDupe)


containsDuplicate([1,2,3,1])

