#Maximum Subarray
#Given an integer array nums, find the subarray with the largest sum, and
#return its sum

def maxSubarray(nums: list)-> int:
    #approach: use window of size of array and scale down window
    windowLower=0
    windowUpper=len(nums)
    windowLength=windowUpper-windowLower
    maxSum=0
    while(windowLength>0):
        windowUpper=windowLower+windowLength
        while(windowUpper<=len(nums)):
            sum=0
            for i in range(windowLower, windowUpper):
                sum+=nums[i]
            if (sum>maxSum):
                maxSum = sum
            windowLower+=1
            windowUpper=windowLower+windowLength
        windowLength-=1
        windowLower=0
    return maxSum

print(maxSubarray([1,2,3,4,-1]))