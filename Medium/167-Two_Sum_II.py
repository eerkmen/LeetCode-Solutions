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
        L, R = 0, len(numbers) - 1

        while L < R:
            curSum = numbers[L] + numbers[R]

            if curSum > target:
                R -= 1
            elif curSum < target:
                L += 1
            else:
                return [L + 1, R + 1]
            