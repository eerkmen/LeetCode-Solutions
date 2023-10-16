#positive integer
#minimal length
#contiguous subarray=a window
#return length of window
#subarray= can be one value, all of the array etc.


#brute force
#try every possible subarray
#nested for loops
#time complexity= O(n^2)
#repeated work is done so not the best option
#looking at the example [2,3,1,2,4,3], our first value taken as the starting point the target value is reached at [2,3,1,2]
#next start at the [3], do [3,1]. BUT we have already calculated this subarray under the first value 2
#we know this bcs we know all of the values are positive, it is never possible to find another valid window before our last added value.


#sliding window
#left pointer,total intialize 0
#initialize minWindow to infinity, this works because any result will overwrite it
#if the total is less than the target value
# increment the right pointer by one
# add the new value at the right pointer to the total
#if the total is equal or more than the target value
# compare the length of the window to the minWindow array take the smaller one
# subtract the left pointer value from the total
# increment left pointer by one
#time complexity: O(n)
#memory complexity: O(1)

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
      L, total = 0, 0
      res = float("inf")

      for R in range(len(nums)):
            total +=nums[r]
            while total >= target:
              res = min(R - L + 1, res)
              total -= nums[L]
              L += 1

      return 0 if res == float("inf") else res