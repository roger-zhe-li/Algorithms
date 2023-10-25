# link to the problem: https://www.lintcode.com/problem/116/description

# Solution 1: Greedy Search
# For each element in the list, check whether it is in the maximum reach (initialized as 0). If it is within reach, update the max reach
# by getting the max of the current max reach and ind + list[ind]. If max_reach is beyond the length, return true. Else return False

# Time complexity: O(n)

from typing import (
    List,
)

class Solution:
    """
    @param a: A list of integers
    @return: A boolean
    """
    def can_jump(self, a: List[int]) -> bool:
        # write your code here
        n = len(a)
        pos = 0
        max_reach = a[0]
        for i in range(n):
            # print(max_reach)
            if i <= max_reach:
                max_reach = max(max_reach, i+a[i])
                if max_reach >= n - 1:
                    return True
            else:
                return False
