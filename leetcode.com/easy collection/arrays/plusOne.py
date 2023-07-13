#you are given a large integer represented as integer array digits where each digits[i] is the ith digit of the integer
#increment the large integer by one and return resulting array of digits

def plusOne(digits: list)-> list:
    digits[len(digits)-1]=digits[len(digits)-1]+1
    for i in range (0, len(digits), 1):
        if (digits[i]==10):
            digits[i]=0
            digits[i-1]+=1
    return digits
