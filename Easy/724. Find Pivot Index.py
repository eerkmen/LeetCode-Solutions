#brute force
#check and compare every subarray
#time complexity: O(n^2)

#prefix sums solution
#calculate prefix array
#for the right side subtract the left sum and pivot, this calculates right sum
 
 class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        leftSum = 0
        for i in range(len(nums)):
           rightSum = total - num[i] - leftSum
           if leftSum == rightSum:
              return i
           leftSum += nums[i]
        return -1