#no duplicate characters
#return length

#brute force
#check every single substring
#loop continues even if there is a duplicate
#need to eliminate repeated work
#time complexity: O(n^2)

#sliding window
#initialize two pointers
#increment left pointer if there is a duplicate
#increment right pointer if there is not a duplicate
#use set to check duplication
#keep record of the longest length of the substring
#remove the duplicate from the set too
#time complexity:O(n)
#memory complexity:O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = 0
        L = 0

        for R in range(len(s)):
            while s[R] in charSet:
                charSet.remove(s[L])
                L += 1
            charSet.add(s[R])
            res = max(res, R- L + 1)
        return res