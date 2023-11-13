#brute force
#check every single combination of container
#time complexity: O(n^2)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0

        for L in range(len(height)):
            for R in range(L + 1, len(height)):
                area = (R - L) * min(height[L], height[R])
                res = max (res, area)
        
        return res
