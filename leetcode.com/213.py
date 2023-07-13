#House Robber 2
#houses are in circle

def houseRobber2(nums: list)->int:
        def rob(arr: list, robIndex: int)->int:
            money=0
            if robIndex == 0:
                arr[robIndex+1]=0
                arr[len(arr)-1]=0
                money=arr[robIndex]
                arr[robIndex]=0
                return money
            elif robIndex == len(arr)-1:
                arr[robIndex-1]=0
                arr[0]=0
                money=arr[robIndex]
                arr[robIndex]=0
                return money
            else:
                arr[robIndex+1]=0
                arr[robIndex-1]=0
                money=arr[robIndex]
                arr[robIndex]=0
                return money
        def max(arr: list)->int:
            max=0
            for element in arr:
                if element>max:
                    max=element
            return max
        maxVal = max(nums)
        totalMoney=0
        while maxVal!=0:
            totalMoney +=rob(nums,nums.index(maxVal))
            maxVal = max(nums)
        return totalMoney

print(houseRobber2([1,2,3]))