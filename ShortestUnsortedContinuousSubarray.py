# Given an integer array, you need to find one continuous subarray 
# that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

# You need to find the shortest such subarray and output its length.

# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.


class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sortlist = sorted(nums)
        if nums == sortlist:
            return 0
        else:
            for i in range(len(nums)):
                if sortlist[i]!=nums[i]:
                    firstIndex = i
                    break
            for i in range(len(nums)-1,-1,-1):
                if sortlist[i] != nums[i]:
                    lastIndex= i
                    break
            return(lastIndex-firstIndex+1)