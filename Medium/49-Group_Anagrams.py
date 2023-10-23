#sorting
#two strings of each other if we take each of them and sort them
#time complexity: O(m * nlogn) => m number of input strings, n is is for each string sorting

#hashmap
#a-z (26)
#ex: eat count [a-z] = e:1, a:1, t:t
#time complexity: O(m*n*26) => O(m*n)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1
              
            res[tuple(count)].append(s)

        return res.values()