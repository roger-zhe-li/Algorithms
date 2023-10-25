# Link to the problem: https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            sign = 1
            s = s[1:]
        else:
            s = s
        
        s_num = ''
        print(s)
        if not s:
            return 0
        elif s[0] < '0' or s[0] > '9':
            return 0
        else:
            for c in s:
                if c >= '0' and c <= '9':
                    s_num += c
                else:
                    break
            res = int(s_num) * sign
            if res > 2 ** 31 - 1:
                res = 2 ** 31 - 1
            elif res < -2 ** 31:
                res = -2 ** 31
            return res
