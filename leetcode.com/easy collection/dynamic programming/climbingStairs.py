#Climbing Stairs
#You are climbing a staircase, it takes n steps to reach the top, each step you can either climb you can either
#climb one or two, how many ways are there to reach the top?

def climbStairs(n: int)->int:
    return arrGen(n)
    
def arrGen(n:int)-> int:
    if n==1:
        return 1
    if n==2:
        return 2
    arr = [1,2]
    for i in range(0, n-2):
        arr.append(0)
    for i in range (2, n):
        arr[i] = arr[i-1]+arr[i-2]
    return arr[n-1]