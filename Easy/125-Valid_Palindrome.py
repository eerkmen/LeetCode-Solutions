#palindrome:reads the same as it does when it is reverse
#ex: aba => aba
#ignore non-alphanumeric characters
#consider all strings as lowerCase
#ignore the space

#iterate through every single character
#if the character.isalnum
# include it.lower in the newstring
#if true return true
#extra memory is needed

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
    

#two pointer method
#keep incrementing left pointer and decrementing the right pointer
#if .isalnum method not allowed to use
#check ASCII values
#while our Left pointer not alphanumerical keep incrementing
#time complexity: O(n)
#memory complexity: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1

        while L < R:
            while L < R and not self.alphaNum(s[L]):
                L += 1
            while L < R and not self.alphaNum(s[R]):
                R -= 1

            if s[L].lower() != s[R].lower():
                return False
            L, R = L + 1, R - 1
        return True



    def alphaNum(self, c):
        return ((ord('A') <= ord(c) <= ord('Z')) or
               (ord('a') <= ord(c) <= ord('z')) or
               (ord('0') <= ord(c) <= ord('9')))