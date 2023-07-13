class PowerOfThree:
    def __init__(self, n:int):
        self.n = n
    def __str__(self):
        num = self.n
        while(num!=1):
            if (num%3!=0):
                return 'False'
            num/=3
        return 'True'
    
obj = PowerOfThree(6)
print(obj)
        