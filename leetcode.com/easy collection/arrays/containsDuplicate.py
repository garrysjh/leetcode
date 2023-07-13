#containsDuplicate
#given an integer array nums, return ture if any value appears at least twice in the array, return
#false if distinct

def containsDuplicate(nums: list)-> bool:
    return len(set(nums))!=len(nums)

print(containsDuplicate([1,2,3,3,4]))