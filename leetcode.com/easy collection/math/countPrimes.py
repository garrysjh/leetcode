#Count Primes
#Given an integer n, return the number of prime numbers that are strictly less than n
#e.g. n=10, there are 4 primes
#primes are 2,3,5,7,11,13,17,19,23,

def countPrimes(n: int)->int:
    if n<=2:
        return 0
    elif n==3:
        return 1
    else:
        count=2
        for i in range(4, n):
            if (i%2!=0) and (i%3!=0):
                count+=1
        return count
    
print(countPrimes(0))