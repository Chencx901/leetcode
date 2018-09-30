Given an array of size n, 
find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

Input: [3,2,3]
Output: 3

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = sorted([(x,nums.count(x)) for x in set(nums)],key = lambda x:x[1],reverse=True)[0][0]
        return a