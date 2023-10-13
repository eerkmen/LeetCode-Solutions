#target - element should be equal to another element that exists in given array
#exactly one solution

#hashmap
#map each value to the index
#initialize hashmap empty
#visited element is checked with the target - element equation. check if it exists in hashmap
#everytime an element is visited add it to hashmap
#gurantees that once the second element that adds up to the total value, first one is already in hashmap
#time complexity: O(n)
#memory complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index

        for i, n in enumerate(nums):
            diff = target -n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[na] = i
        return
    
#brute force
#check every combination for every element
#time complexity: O(n^2)
