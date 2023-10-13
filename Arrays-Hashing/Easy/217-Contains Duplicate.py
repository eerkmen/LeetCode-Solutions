#hashset
#extra memory compared to other solutions
#insert elements O(1)
#at the beginning empty hashset
#Every time a new element is checked add it to hashset
#if an element already exists return true
#time complexity: O(n) => each operation O(1), do it for every element in the input array once
#space complexity: O(n) => create a new hashset
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

#sorting
#compare adjacent elements
# time complexity: one pass O(n) but sorting is O(nlogn) => O(nlogn)
# space complexity: O(1) = constant time




#brute force method
#chech every single number against each other
#time complexity: O(n^2)
#space complexity: O(1)/constant time
