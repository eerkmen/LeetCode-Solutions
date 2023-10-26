#easy if no division restriction
#multiply all numbers
#divide it by the current index


#multiply every value before the selected value(prefix)
#multiply every value after the selected value(postfix)
#multiply them (output)
#if no prefix or postfix value exists take it as 1
#EXAMPLE: selected value is (X)
#input:1,2,3(X),4
#prefix:1,2(X),6,24
#postfix:24,24,12,4(X)
#output:24,12,8(X),6
#time complexity: O(n)
#space complexity: O(n)

#space complexity can be better using the previous idea
#no need to create prefix,postfix array. store in output array memory
#iterate through input array from index 0 to store prefix values in output array
#iterate(decrement) throught input array from last index to multiply postfix values to output array values
#EXAMPLE:
#input:1,2,3(X),4
#output:first pass =>1,1,2,6 second pass => 24, 12, 8, 6
#time complexity: O(n)
#space complexity: O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res