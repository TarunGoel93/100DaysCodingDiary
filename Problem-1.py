# Sum Of Digits

class Solution:
    def sumOfDigits(self, n):
        sum = 0
        while(n!=0):
            digit = n%10
            sum+=digit
            n = n//10
        return sum
sol = Solution()
print(sol.sumOfDigits(1))