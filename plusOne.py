# Given a non-empty array of digits representing a non-negative integer, 
# plus one to the integer.
# The digits are stored such that the most significant digit 
# is at the head of the list, and each element in the array contain a single digit.
# You may assume the integer does not contain any leading zero, 
# except the number 0 itself.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = list(reversed(digits))
        l[0] += 1
        i,c = 0,0
        while i < len(l):
            c1 = (l[i]+c)//10
            l[i] = (l[i]+c)%10
            i,c = i+1,c1
        if c1 > 0:
            l.append(1)
        return list(reversed(l))