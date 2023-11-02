#brute force
#check every single subarray
#time complexity: O(n^2)

#kadanes/sliding window
#initialize left and right pointer
#compare index R with R-1
#if R and R-1 is equal: put left pointer to the current right pointers index, increment R by one
#if turbulence: greater than and less than order is false: shift left pointers index to R-1's index
#time complexity: O(n)
#space complexity: O(1)

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        