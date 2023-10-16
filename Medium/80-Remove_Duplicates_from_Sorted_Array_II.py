#non-decreasing order
#in-place
#allowed to have maximum two copies of a value
#overwrite the third copy with other duplicates that come after it
#a pointer will return the index, which will be the size of the array



#initialize L,R pointer from index 0
#if R pointer on the third copy
# increment L pointer
# put the R pointer on the same index as L

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L, R = 0, 0

        while R < len(nums):
          count = 1
          while R + 1 < len(nums) and nums[R] == nums[R + 1]:
              R +=1
              count += 1
              
          for i in range(min (2, count)):
            nums[L] = nums[R]
            L += 1
          R += 1
        return L