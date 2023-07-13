#richest customer wealth
#you are given an m x n integer grid accounts where accounts[i][j] is the amount of money
#the ith customer has in the jth bank
#return highest wealth

def richestWealth(accounts: list) -> int:
    wealthDict = {}
    for i in range(0,len(accounts)):
        wealth=0
        for j in range(0,len(accounts[i])):
            wealth+=accounts[i][j]
        wealthDict[f'{i}'] = wealth
    return maxValueFromDict(wealthDict)
        
            

def maxValueFromDict(thisdict: dict) -> int:
    keyList = thisdict.keys()
    valueList = list(thisdict.values())
    maxValue = valueList[0]
    for key, values in thisdict.items():
        if thisdict[key] > maxValue:
            maxValue = thisdict[key]
    return maxValue

accounts=[[1,2,3],[3,2,1],[3,2,2]]
print(richestWealth(accounts))

