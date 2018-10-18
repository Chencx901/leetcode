# Given an array with n integers, your task is to check if 
# it could become non-decreasing by modifying at most 1 element.
# We define an array is non-decreasing if array[i] <= array[i + 1] 
# holds for every i (1 <= i < n).


class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        index = None
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                if index is not None: # more than one 
                    return False
                index = i
        
        return (index is None or index==0 or index ==len(nums)-2 or 
               nums[index-1]<=nums[index+1] or nums[index]<=nums[index+2])