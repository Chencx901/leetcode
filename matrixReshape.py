# In MATLAB, there is a very useful function called 'reshape', 
# which can reshape a matrix into a new one with different size but 
# keep its original data.
# You're given a matrix represented by a two-dimensional array, 
# and two positive integers r and c 
# representing the row number and column number of the wanted reshaped matrix, respectively.
# The reshaped matrix need to be filled with all the elements of the 
# original matrix in the same row-traversing order as they were.
# If the 'reshape' operation with given parameters is possible and legal, 
# output the new reshaped matrix; Otherwise, output the original matrix.
# Example 1:
# Input: 
# nums = 
# [[1,2],
#  [3,4]]
# r = 1, c = 4
# Output: 
# [[1,2,3,4]]
# Explanation:
# The row-traversing of nums is [1,2,3,4]. 
# The new reshaped matrix is a 1 * 4 matrix, fill it row by row b


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        nr = len(nums)
        nc = len(nums[0])
        if nr*nc != r*c:
            return nums # if can't reshape,return original
        else:
            element = []
            trans = [[0]*c for i in range(r)] # get the trans structure,fill with 0
            for item in nums:
                element += item # get element
            for index,n in enumerate(element):
                rindex = index/c
                cindex = index%c
                trans[rindex][cindex] = n
        return trans