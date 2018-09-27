# Given a matrix A, return the transpose of A.
# The transpose of a matrix is the matrix 
# flipped over it's main diagonal, 
# switching the row and column indices of the matrix.
# Example 1:
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]

class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m,n = len(A),len(A[0])
        ans = [[0]*m for x in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][j] = A[j][i]
        return ans
        