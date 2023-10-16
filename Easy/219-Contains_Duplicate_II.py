#size of the window less or equal to k
# k + 1 is equal to valid window
#return boolean


#brute force
#check every single window



#hashset/hashmap
#look at values in O(1)
#sliding window
#if window is bigger than k
# remove the value in index L
# increment L by 1
#check every value in index R
#if true found duplicate
#otherwise add the value


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
            