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
        L, R = 0, 1
        res, prev = 1, ""

        while R < len(arr):
            if arr[R - 1] > arr[R] and prev != ">":
                res = max(res, R - L + 1)
                R += 1
                prev = ">"
            elif arr[R - 1] > arr[R] and prev != "<":
                res = max(res, R - L + 1)
                R += 1
                prev = "<"
            else:
                R = R + 1 if arr[R] == arr[R - 1] else R
                L = R - 1 
                prev = ""
        return res