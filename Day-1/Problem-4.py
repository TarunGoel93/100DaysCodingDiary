# Prime Number

class Solution:
  def isPrime(self, n):
    count = 0
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1,1):
      if n%i==0:
        count+=1
        break
    if count==0:
      return True
    else:
      return False
sol = Solution()
print(sol.isPrime(1))
