#t and s must
#have same number of characters
#exact same characters


#hashmap
#two hashmaps
#key: character, value: number of appearences
#after hashmaps created compare them against each other
#time complexity: O(n) => O(s+t) but considering they are the same length so O(2n) and 2 is constant
#memory complexity: O(n) => same as time complexity
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, contT = {}, {}

        #build hashmap
        for i in range(len(s)):
            #if the key doesn't exist get returns default value as 0
            countS[s[i]] = 1 + counstS.get(s[i], 0)
            countS[t[i]] = 1 + counstS.get(t[i], 0)
        
        for c in countS:
            #get used for situation key not existing in t
            if counstS[c] != countT.get(c, 0):
                return False
        return True

#counter data structure
#hashmap that counts automatically
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    

#sorted
#Space complexity: O(1)
#time complexity: O(nlogn)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)