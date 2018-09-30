# Given an integer array nums, 
# find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.
# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        init_val = nums[0]
        max_sum = nums[0]
        for i in range(1,len(nums)):
            curr = max(init_val + nums[i], nums[i])
            init_val = curr
            if max_sum < curr: max_sum = curr
        return max_sum
