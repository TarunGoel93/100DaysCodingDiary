#Happy Number

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while(n!=1 and n not in seen):
            seen.add(n)
            sum = 0
            while n>0:
              digit = n%10
              sum+=digit*digit
              n = n//10
            n = sum
        return n==1

sol = Solution()
print(sol.isHappy(19))

