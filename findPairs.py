# Given an array of integers and an integer k, 
# you need to find the number of unique k-diff pairs in the array. 
# Here a k-diff pair is defined as an integer pair (i, j), 
# where i and j are both numbers in the array and their absolute difference is k.
# Example 1:
# Input: [3, 1, 4, 1, 5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number 
# of unique pairs.

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k>0:
            return len(set(nums)&set(n+k for n in nums))
        elif k==0:
            return sum(v>1 for v in collections.Counter(nums).values())
        else:
            return 0