# Factorial

class Solution:
  def factorial(self, n: int) -> int:
    mul = 1
    for i in range(n,0,-1):
      mul*=i
    return mul
sol = Solution()
print(sol.factorial(5))