#given 2 sorted arrays nums1 and nums2 of size m and n respectively, return median of 2 arrays
#time complexity must be O(log(m+n))
#input nums1=[1,3] nums2=[2]

def medianOfTwo(nums1: list, nums2: list) -> int:
    for element in nums2:
        nums1.append(element)
    nums1.sort()
    if(int(len(nums1))/2==0):
        return float((nums1[int(len(nums1)/2)]+nums1[int(len(nums1)/2)-1])/2)
    else:
        return nums1[int(len(nums1)/2)]

nums1=[1,3]
nums2=[2,6,5]

print(medianOfTwo(nums1,nums2))
