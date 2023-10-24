# link to the problem: https://www.lintcode.com/problem/407/

# Solution 1: based on list operations. 
# initialize a carry and make it as 1. calculate from the last digit. if carry + digit >= 10, then make carry as 1 again, otherwise 0. 
# in the meantime, get the mod as the new digit
# in the end, if carry is 1, then add another 1 at the beginning of the list
# beats 84%

from typing import (
    List,
)

class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """
    def plus_one(self, digits: List[int]) -> List[int]:
        # write your code here
        n = len(digits)
        carry = 1
        for i in range(n-1, -1, -1):
            carry, digits[i] = (digits[i] + carry) // 10, (digits[i] + carry) % 10
            
        if carry == 0:
            return digits
        else:
            return [1] + digits



# Solution 2: type switch between int and str
# turn list of numbers into a string and back to list, then +1
# turn the +1 list to string and transform all characters back to int
# very slow, just for exercising. beats 13%

class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """
    def plus_one(self, digits: List[int]) -> List[int]:
        # write your code here
        str_digit = ''.join(str(digit) for digit in digits)
        new_digit = int(str_digit) + 1
        new_list = list(str(new_digit))
        return [int(i) for i in new_list]
