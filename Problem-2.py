# Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        original_num = x
        if x<0:
            x = abs(x)
        rev = 0
        while(x!=0):
            digit = x%10
            rev = rev*10+digit
            x = x//10
        if original_num<0:
            rev =  -rev
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev
sol = Solution()
print(sol.reverse(-123))