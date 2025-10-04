# Fibonacci Number

class Solution:
    def fib(self, n: int) -> int:
        if n==1:
            return 1
        if n==0:
            return 0

        a = 0
        b = 1
        x = [a,b]
        for i in range(2,n+1,1):
            f = a+b
            x.append(f)
            a = b
            b = f
        return x[n]
        