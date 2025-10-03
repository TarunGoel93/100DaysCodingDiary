# Area of a Circle

import math
class Solution:
  def calculateArea(self,r):
    pie = math.pi
    return pie*r*r
sol = Solution()
print(sol.calculateArea(5))