# Given a binary array, find the maximum number of consecutive 1s in this array.
# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: 
# The first two digits or the last three digits are consecutive 1s.
# The maximum number of consecutive 1s is 3.

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        prev = []
        for x in nums:
            if x == 1:
                count += 1
            else:
                prev.append(count)
                count = 0
        prev.append(count)
        return max(prev)
                