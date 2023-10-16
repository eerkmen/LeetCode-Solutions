#in-place algorithm
#take all of the values that are not special value placed at the beginning
#relative order does not matter

#two pointer method
#left pointer is where we replace the values at
#to increment left pointer
#if the value the left pointer is at is not the special value, just swap it by itself and increment it by one
#this way we don't have to think about edge cases calculating the result

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L = 0

        for R in range(len(nums)):
            if nums[R] != val:
                nums[L] = nums [R]
                L += 1
        return L
