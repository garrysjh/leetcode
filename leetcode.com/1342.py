#Number of steps to reduce a number to zero
##gien an integer num, return number of steps to redue it to zero
#if odd, -1, if even /2
def reduceToZero(num: int):
    num=num
    steps=0
    while (num!=0):
        if (num%2==0):
            num/=2
            steps+=1
        if (num%2!=0):
            num-=1
            steps+=1
    return steps
     

print(reduceToZero(14))

