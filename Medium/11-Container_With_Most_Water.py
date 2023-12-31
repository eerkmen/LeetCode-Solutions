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


#two pointer method
#initialize Left at the beginning
#initialize Right at the end
#compare elements in left and right index
#minimum one would be increment/decrement
#time complexity: O(n)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        L, R = 0, len(height) - 1

        while L < R:
            area = (R - L) * min(height[L], height[R])
            res = max (res, area)

            if height[L] < height[R]:
                L += 1
            else:
                R -= 1

        return res