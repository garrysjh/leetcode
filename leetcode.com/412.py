# given an integer n, return a string array answer where:
#answer[i] = fizzbuzz if i is divisible by 3 and 5

def fizzbuzz(n: int) -> list:
    list = []
    for i in range(1, n+1):
        if (i%3==0) & (i%5==0):
            list.append("FizzBuzz")
        elif i%3==0:
            list.append("Fizz")
        elif i%5==0:
            list.append("Buzz")
        else:
            list.append(i)
    return list

n = 15
print(fizzbuzz(n))