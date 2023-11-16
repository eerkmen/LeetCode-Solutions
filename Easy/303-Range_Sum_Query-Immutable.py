#brute force
#time complexity: O(n)

#doing precomputation will make query faster
#it will make it constant time
#creating all of the subarray calculations will make it time complexity:O(n^2)
#but it will only run once in the beginning

#better solution
#computing prefix sums
#time complexity: O(n) of creating prefix sum
#create a prefix sum array
#Right index - (left index - 1) of prefix sum array is the result 
#check if left index - 1 is in bounds
#time complexity: O(1)