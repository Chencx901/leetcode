# template 1: 
'''search for an element or condition which can be determined by accessing a 
single index in the array.
'''
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0: # special condition
        return -1

    left, right = 0, len(nums) - 1   # assign left and right index
    while left <= right:             # end condition: left > right
        mid = (left + right) // 2    # mid
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1

# example : int sqrt(int x):
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1 or x == 0:
            return x
        h = x
        l = 0
        while h - l > 1:
            mid = (l+h)//2
            mm = mid**2
            if x > mm:
                l = mid
            elif x == mm:
                return mid
            else:
                h = mid
        return l

# example:Search in Rotated Sorted Array
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

class Solution:
    def search(self, nums, target):
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            #  one part is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

# Template II:
'''
search for an element or condition which requires accessing 
the current index and its immediate right neighbor's index in the array.
'''
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    # Post-processing:
    # End Condition: left == right
    if left != len(nums) and nums[left] == target:
        return left
    return -1

# example 1: first bad
'''
Suppose you have n versions [1, 2, ..., n] and you want to 
find out the first bad one, which causes all the following ones to be bad
'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low,high = 1,n
        while low <= high:
            mid = (low+high)//2
            if isBadVersion(mid) == True:
                if isBadVersion(mid-1) ==False:
                    return mid
                else:
                    high = mid
            else:
                low = mid+1

# example 2: A peak element is an element that is greater than its neighbors.
# Given an input array nums, where nums[i] ≠ nums[i+1], 
# find a peak element and return its index.
# The array may contain multiple peaks, 
# in that case return the index to any one of the peaks is fine.

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Conditions:
     1. array length is 1  -> return the only index 
     2. array length is 2  -> return the bigger number's index 
     3. array length is bigger than 2 -> 
           (1) find mid, compare it with its left and right neighbors  
           (2) return mid if nums[mid] greater than both neighbors
           (3) take the right half array if nums[mid] smaller than right neighbor
           (4) otherwise, take the left half
        """
        left = 0 
        right = len(nums)-1
        # condition 3
        while left < right-1:
            mid = (left+right)/2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            
            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid-1
        # condition 1&2
        if nums[left] >= nums[right]:
            return left
        else:
            return right

''' example 3:
Suppose an array sorted in ascending order is rotated at some 
pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
'''
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        left, right = 0, size - 1
        if(nums[left] < nums[right]): # no rotation
            return nums[left]

        while left + 1 < right:
            mid = (left + right) // 2

            if(nums[mid] > nums[left]):
                left = mid
            elif(nums[mid] < nums[right]):
                right = mid

        if nums[left] < nums[right]:
            return nums[left]
        else:
            return nums[right]

# template 3:
'''
 search for an element or condition which requires accessing the 
 current index and its immediate left and right neighbor's index in the array.

'''
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid

    # Post-processing:
    # End Condition: left + 1 == right
    if nums[left] == target: return left
    if nums[right] == target: return right
    return -1

# example 1: Search for a Range
'''
Given an array of integers nums sorted in ascending order, 
find the starting and ending position of a given target value.
If the target is not found in the array, return [-1, -1]
'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        first = float("inf")
        second = float("-inf")
        
        low = 0
        high = len(nums)-1
        
        while(low<=high):
            mid = (low+high)/2
            if nums[mid] == target:
                first = min(first,mid)
                high = mid-1 # Search left to get min index
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid+1
                  
        low = 0
        high = len(nums)-1

        # Reset the variables low and high
        while(low<=high):
            mid = (low+high)/2
            if nums[mid] == target:
                second = max(second,mid)
                low = mid+1 #Search right to get the max index.
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid+1
        first = first if first!=float("inf") else -1
        second = second if second!=float("-inf") else -1
            
        return [first,second]

# example 2: Find K Closest Elements
'''
Given a sorted array, two integers k and x, 
find the k closest elements to x in the array. 
The result should also be sorted in ascending order. 
If there is a tie, the smaller elements are always preferred.
Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
'''
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        idea: find start element,return [start,start+k]
        """
        lo, hi = 0, len(arr)-k # initial 
        while lo<hi:
            mid = (lo + hi)//2
            if x-arr[mid]>arr[mid+k]-x: # if there has tie
                lo = mid + 1
            else:
                hi = mid
        return arr[lo:lo+k]

# pow(x,n)
class Solution:
    def myPow(self, a, b):
        if b == 0: return 1 # base line
        if b < 0: return 1.0 / self.myPow(a, -b)
        half = self.myPow(a, b // 2)
        if b % 2 == 0:
            return half * half
        else:
            return half * half * a