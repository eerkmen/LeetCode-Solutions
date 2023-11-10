#palindrome:reads the same as it does when it is reverse
#ex: aba => aba
#ignore non-alphanumeric characters
#consider all strings as lowerCase
#ignore the space

#iterate through every single character
#if the character.isalnum
# include it.lower in the newstring
#if true return true

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]