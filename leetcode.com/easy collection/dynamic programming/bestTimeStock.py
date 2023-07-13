#Best time to sell stock
#You are given an array prices, where prices[i] is the price of a given tsock
#on the ith day
#You want to maximize your profit by choosing a single day to buy one stock
#and choosing a different dayin the future to sell that stock
#Return the maximum profit you can achieve from this transaction

def bestTime(prices: list)-> int:
    maxProfit = 0
    for i in range(0, len(prices)):
        for j in range(i+1, len(prices)):
            if(prices[j]-prices[i])>maxProfit:
                maxProfit = prices[j]-prices[i]
    return maxProfit

print(bestTime([7,1,5,3,6,4]))