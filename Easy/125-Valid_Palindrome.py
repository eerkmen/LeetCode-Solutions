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