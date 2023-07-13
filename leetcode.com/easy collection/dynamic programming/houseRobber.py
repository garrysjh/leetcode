#House Robber
#You are a professional robber planning to rob houses along the street. Each house has a certain amount of money
#stashed
#Basically, avoid 2 adjacent houses 
#Given an integer array nums, representing teh amount of mone of each house,
#return max amount of money you can rob tonight
def houseRobber(nums: list)-> int:
    def rob(arr: list, houseIndex: int)-> int:
        robbed = arr[houseIndex]
        arr[houseIndex]=0
        if houseIndex!=0:
            arr[houseIndex-1]=0
        if houseIndex!=len(arr)-1:
            arr[houseIndex+1]=0
        return robbed
    #find max
    def maximize(arr:list)-> int:
        max=0
        for element in arr:
            if element>max:
                max = element
        return max
    max=maximize(nums)
    totalMoney=0
    while max!=0:
        max=maximize(nums)
        totalMoney+=rob(nums,nums.index(max))
    return totalMoney

print(houseRobber([2,7,9,3,1]))
    
