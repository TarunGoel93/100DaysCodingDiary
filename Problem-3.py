# Palindrome Number

# x = 121

class Solution:
    def isPalindrome(self, x: int) -> bool:
        orignal_num = x
        rev = 0
        if x<0:
            return False
        while(x!=0):
            digit = x%10
            rev = (rev*10)+digit
            x = x//10
        if orignal_num==rev:
            return True
        else:
            return False
sol = Solution()
print(sol.isPalindrome(-121))
        