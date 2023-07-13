#given two integer arrays of nums1 and nums2, return an array of their intersection
#each element in the result must appear as many times as it shows in both arrays and you may return the result
#in any order

def intersectionOfTwoArrays(nums1: list, nums2: list)-> list:
    intersection = []
    for i in range(0, len(nums1)-1):
        for j in range(0, len(nums2)-1):
            if nums1[i]==nums2[j]:
                intersection.append(nums1[i])
    return intersection

print(intersectionOfTwoArrays([1,2,3,4],[2,3]))