# Leap Year

class Solution:
    def checkYear (self, n):
        if n%100!=0 and n%4==0:
            return True
        elif n%100!=0 and n%4!=0:
            return False
        elif n%400==0:
            return True
        else:
            return False
sol = Solution()
print(sol.checkYear(2000))