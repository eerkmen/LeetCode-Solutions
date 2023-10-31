#circular= end connected to beginning
#max subarray sum can have portion from end and the beginning

#kadanes algorithm
#be greedy as possible
#keep tack of curMax, update globalMax using curMAx
#edgecase: globalMax must be initialized to any value, if initialized to 0  array with all negative values will give an error
#compare curSum to the value we are at and update curMax using the max value

#handling circular requirement
#if global min contigious subarray sum is known, we can totalsum-globalMin

#edge case: if every value is negative, total - globalMin = 0
#check if globalMax < 0 then return max value in the array

#time complexity: O(n)

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        