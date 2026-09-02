class Solution:
    def isHappy(self, n: int) -> bool:
        s, f = n, self.Sumsquare(n)

        while f!=1 and s != f:
            s, f = self.Sumsquare(s) , self.Sumsquare(self.Sumsquare(f))

        return f == 1
    
    def Sumsquare(self , n)-> int :
        s= 0
        while n:
                m = n%10
                s+= m**2
                n = n//10
        return s