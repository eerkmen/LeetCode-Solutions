#iterate through each value and append it to the end of array
#time complexity: O(n)

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range (2):
            for n in nums:
                ans.append(n)
        return ans