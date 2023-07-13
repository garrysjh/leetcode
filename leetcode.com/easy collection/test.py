class Solution:
    def minCost(self, nums: list[int], cost: list[int]) -> int:
        #check cost for each individual element in 
        #assuming u change it all to the first element in nums
        costsArr = []
        for i in range (0, len(nums)):
            costed=0
            for j in range(0, len(nums)):
                if i!=j:
                    difference = abs(nums[j]-nums[i])
                    costed += difference*cost[j]
            costsArr.append(costed)
        return min(costsArr)

solution = Solution()
#Supposed to output: [24,20,56,8]
print(solution.minCost(nums=[1,3,5,2], cost=[2,3,1,14]))