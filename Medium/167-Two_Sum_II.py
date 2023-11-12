#brute force
#look every combination
#time complexity: O(n^2)

#two pointer method
#initialize Left pointer at the beginning
#initialize Right pointer at the end
#if total sum is bigger than target
# decrement right pointer by 1
# if total sum is smaller than target
# increment Left pointer by 1
#return indeces
#time complexity: O(n)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        