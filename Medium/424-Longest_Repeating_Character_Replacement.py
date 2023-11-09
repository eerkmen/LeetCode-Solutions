#return length of subarray

#brute force
#check every single subarray
#how to decide which character to replace
#replace the least common character
#use hashmap to count the occurences
#windowLength - count[most frequent character] = number of characters we need to replace
#so this calculation must be equal or less than k
#if this conidition is true our window is valid
#how to know which character is the most frequent
# check every character in hashmap O(26 * n)


#sliding window
#if the mentioned condition is valid
#increment right pointer
#update hashmap - add character count by one
#update the result length
#if not increment left pointer
#update hashmap- remove the character from the count
#time complexity: O(n) => actually O(26 * n) due to checking throught hashmap

#another way to do it without checking through all of the hashmap to find the most frequent character
#maxFrequency is created and saved
#result will be maximized only if new maxFrequency is found that is bigger than the current so no need to decrement it whenever left pointer is incremented
#more complicated solution
#time complexity: O(n) => compared to the previous sliding window solution actually O(n) there is no constant

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        L = 0
        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)

            while (R - L +1) - max(count.values()) > k:
                count[s[L]] -= 1
                L += 1
            res = max(res, R - L +1)
        return res
    

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        L = 0
        maxf = 0
        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            maxf = max(maxf, count[s[R]])
            
            while (R - L +1) - maxf > k:
                count[s[L]] -= 1
                L += 1
            res = max(res, R - L +1)
        return res