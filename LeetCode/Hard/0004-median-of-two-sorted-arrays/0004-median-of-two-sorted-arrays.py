class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp = nums1 + nums2
        temp.sort()
        if not len(temp) % 2:#even
            result = temp[len(temp)//2] + temp[len(temp)//2 - 1]
            return result/2
        else:#odd
            return temp[len(temp)//2]