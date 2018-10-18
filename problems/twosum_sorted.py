# Given an array of integers that is already sorted in ascending order, find two
# numbers such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers 
# such that they add up to
# the target, where index1 must be less than index2.

# Example:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """  
        dic = {}
        for index,num in enumerate(numbers):
            if target - num in dic:
                return [dic[target-num]+1,index+1]
            dic[num] = index