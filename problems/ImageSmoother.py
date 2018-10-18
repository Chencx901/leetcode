# Given a 2D integer matrix M representing the gray scale of an image, 
# you need to design a smoother to make the gray scale of each cell becomes the average gray scale 
# (rounding down) of all the 8 surrounding cells and itself. 
# If a cell has less than 8 surrounding cells, then use as many as you can.

# Input:
# [[1,1,1],
#  [1,0,1],
#  [1,1,1]]
# Output:
# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]
# Explanation:
# For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# For the point (1,1): floor(8/9) = floor(0.88888889) = 0

class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        R = len(M) # row length
        C = len(M[0]) # col length
        res = [[0]*C for _ in range(R)] # create empty matrix
        for x in range(R):
            for y in range(C):
                #  find neighbour 
                neighbour = [
                    M[_x][_y]
                    for _x in (x-1, x, x+1)
                    for _y in (y-1, y, y+1)
                    if 0 <= _x < R and 0 <= _y < C
                ]
                res[x][y] = sum(neighbour) // len(neighbour)
        return res