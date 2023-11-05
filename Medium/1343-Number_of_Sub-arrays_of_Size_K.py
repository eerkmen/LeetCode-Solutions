#sliding window
#threshold =average greater or equal 
#intialize Left, Right pointers
#keep track of currentsum
#if average lower than threshold
#increment Right pointer by one
#add value at right pointer to currentsum
#if average is greater or equal to threshold
#increment the left pointer by one
#subtract the value from the current sum
#memory complexity: O(1)

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        curSum = sum(arr[:k-1])

        for L in range(len(arr) - k + 1):
          curSum += arr[L + k -1]
          if (curSum / k) >= threshold:
             res+=1
          curSum -= arr[L]
        return res