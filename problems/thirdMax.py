# Given a non-empty array of integers, return the third maximum number 
# in this array. If it does not exist, return the maximum number. 
# The time complexity must be in O(n).
# Example 1:
# Input: [3, 2, 1]
# Output: 1
# Explanation: The third maximum is 1.

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # no third max number
        if len(set(nums)) < 3:
            return (max(set(nums)))
        else:
            sort_num = sorted(set(nums),reverse = True)
            return sort_num[2]