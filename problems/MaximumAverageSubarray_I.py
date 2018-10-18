# Maximum Average Subarray I
# Given an array consisting of n integers, 
# find the contiguous subarray of given length k 
# that has the maximum average value. 
# And you need to output the maximum average value.

class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
#       sum first k elements
        sums = 0
        for i in range(0,k):
            sums += nums[i]
        res = sums
#       sliding windows
        for i in range(k,len(nums)):
            sums += nums[i] - nums[i-k]
            res = max(res,sums)
        return res/k