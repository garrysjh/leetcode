#Shuffle an array
#Given an integer array nums, design an algorithm to randomly shuffle the array.
#All permutations of the array should be equally likely as a result of the shuffling
import random
class Solution:
    def __init__(self, nums: list[int]):
        self.nums = nums
    def reset(self)->list[int]:
        return str(self.nums)
    def shuffle(self)->list[int]:
        length= len(self.nums)
        arr = self.nums
        shuffled = []
        for i in range(0, length):
            num = random.choice(arr)
            shuffled.append(num)
            arr.remove(num)
        return shuffled
    def __str__(self):
        return str(self.nums)

obj = Solution([1,2,3,4])
print(obj.nums)
obj.reset
print(obj)
print(obj.shuffle())
print(obj.reset())