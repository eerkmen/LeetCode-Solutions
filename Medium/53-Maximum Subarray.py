#brute force
#iterate through every single subarray
#time complexity: O(n^3)
#pseudocode:
#starting value=i
for(i=0...n-1):
#j is ending index
  for(j=i ...n-1):
#k=computing sum of the array
    for(k=i...j):
      compute the sum

#to save time
#create currenSum add add the j
#time complexity: O(n^2)
#pseudocode:
for(i=0...n-1)
  for(j=i...n-1)
    curSum + num[j]

#to save more time
#sliding window
#ignore the negative values
#if the sum is greater than 0 keep adding
#else restart the sum from the next element
#time complexity: O(n)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums [0]
        curSum = 0

        for n in nums:
           if curSum < 0:
              curSum = 0
            curSum += n
           maxSub = max(maxSub, curSum)
        return maxSub