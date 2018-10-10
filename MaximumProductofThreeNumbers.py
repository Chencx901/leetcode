# # Given an integer array, find three numbers whose product 
# # is maximum and output the maximum product.

# Example 2:
# Input: [1,2,3,4]
# Output: 24

class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 3:
            return nums[0]*nums[1]*nums[2]
        else:
            l = sorted(nums)
            return max(l[0]*l[1]*l[-1],l[-3]*l[-2]*l[-1])