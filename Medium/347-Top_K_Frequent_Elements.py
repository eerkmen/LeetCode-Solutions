#hashmap
#put repeating elements in hashmap
#hashmap values increment by one everytime input element is repeated 
#sort it
#time complexity: O(nlogn)

#maxheap
#heapify
#each pop logn time complexity
#do it k times
#time complexity: O(klogn)

#bucket sort
#initialize an array
#use the input array value as an index
#intialized array's elements will be the number of times the element appears in input array
#problem: if the input array element is a big number like a 1000 they would be the index 1000 in bucket sort array
#space complexity bad

#CHOSEN SOLUTION
#bucket sort
#the inverse way
#index of bucket sort of array will be the number of time an input element appears
#bucket sort array values will contain input array values sorted in the number of times they appear
#bucket sort array index size is bounded by the input array as it can't be bigger than input array
#after bucket sort array populated, start checking values from the last index and keep on decrementing until k number of elements found
#time complexity: O(n),linear time => if every single value is distinct every one of the input array values will be at the first index of bucket sort array. Iterating over the whole array
#actually it is O(n + n) but we don't count constants
#space complexity: o(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        