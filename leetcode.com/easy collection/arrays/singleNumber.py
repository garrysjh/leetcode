#given a non empty array of intege nums, veery element appears twice except for one
#find that single one

def singleNumber(nums: list)-> int:
    newArr = []
    for element in nums:
        if element not in newArr:
            newArr.append(element)
        else:
            newArr.remove(element)
        
    return newArr[0]

print(singleNumber([1,1,2,2,3,3,4]))