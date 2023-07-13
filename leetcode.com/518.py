#Coin Change II
#Given an integer array coins and amount return number of combinations that make up the amount

#e.g. amount = 5
#coins = 1,2,5
#answer = 4

#approach:
#check 1 type of coin only
#check 2 types of coin
#check 3 types of coin

def coinChangeII(coins: list, amount: int):
    combinations=0
    #remove coin sizes that are too big to reduce computation time
    for element in coins:
        if element>amount:
            coins.remove(element)
    #check combinations for 1 type of coin
    for element in coins:
        if amount%element==0:
            coins+=1
    #check combinations for 2 types of coin
    for i in range(0,len(coins)-1):
        for j in range(0,len(coins)-1):
            if i!=j:
                print()
