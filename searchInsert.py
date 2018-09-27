# Given a sorted array and a target value, 
# return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.
# Example 1:
# Input: [1,3,5,6], 5
# Output: 2

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return [index for index,value in enumerate(nums) if value == target][0]
        elif target < min(nums):
            return 0
        elif target > max(nums):
            return len(nums)
        else:
            res = [x-target for x in nums]
            return [index for index,value in enumerate(res) if value >0][0]

# for i, num in enumerate(nums):
# if num >= target:
# return i
# return len(nums)