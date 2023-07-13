#given an integer array prices where prices[i] is the price of a given stock on the ith day
#find maximum achievable profit

#e.g. [1,2,3,4]
#highest return = 4-1=3
#e.g. [7,1,4,5,9]
#highest return will be 8 = 9-1

def maxProfit(prices: list) -> int:
    max = (prices[1] - prices[0])
    #assuming only one buy and sale
    for i in range(0,len(prices)-1):
        for j in range(i,len(prices)-1):
            if(i!=j):
                if(max<(prices[j]-prices[i])):
                    max=(prices[j]-prices[i])
    #assume multiple buy and sales
    if len(prices)>3:
        print()

    return max