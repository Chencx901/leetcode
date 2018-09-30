# Given an array of integers and an integer k, 
# find out whether there are two distinct indices i and j in the array 
# such that nums[i] = nums[j] and the absolute difference between i and j is 
# at most k.

# Input: nums = [1,2,3,1], k = 3
# Output: true

# Input: nums = [1,0,1,1], k = 1
# Output: true

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for index,val in enumerate(nums):
            if val not in dic:
                dic[val] = index
            elif index - dic[val] <= k:
                return True
            else:
                dic[val] = index
        return False