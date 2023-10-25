# link to the problem: https://www.lintcode.com/problem/1141/

# solution: for all other months other than Feb, return the days by even or odd and their comparison to 6
# for Feb, first judge whether it is a leap year, if yes return 29 else 28
# leap is done via another function (mind the self init)

class Solution:
    """
    @param year: a number year
    @param month: a number month
    @return: return the number of days of the month.
    """
    def get_the_month_days(self, year: int, month: int) -> int:
        # write your code here
        if month % 2 == 1 and month <= 7:
            return 31
        elif month % 2 == 1 and month > 7:
            return 30
        elif month % 2 == 0 and month > 2 and month <= 6:
            return 30
        elif month % 2 == 0 and month > 6:
            return 31
        else:
            if self.leap(year):
                return 29
            else:
                return 28
            
    def leap(self, year):
        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
            return True
        return False
        
