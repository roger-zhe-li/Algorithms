# link to the problem: https://www.lintcode.com/problem/146/

# 2 solutions either using the .upper() method or doing the traditional string operations like in C.
# note: in Python we need to translate the char to int by ord() and then do lower-upper translation.
# finally translate back via chr()

# Solution 1: traditional
class Solution:
    """
    @param letters: A string
    @return: A string
    """
    def lowercase_to_uppercase2(self, letters: str) -> str:
        # write your code here
        n = len(letters)
        res = ""
        for i in range(n):
            if letters[i] >= 'a' and letters[i] <= 'z':
                res += chr(ord(letters[i]) + ord('A') - ord('a'))
            else:
                res += letters[i]
        return res
      

# Solution 2: Pythonic
class Solution:
    """
    @param letters: A string
    @return: A string
    """
    def lowercase_to_uppercase2(self, letters: str) -> str:
        # write your code here
        return letters.upper()
        
