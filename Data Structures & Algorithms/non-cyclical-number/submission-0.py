class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        s=0
        m=n

        while n not in visit: 
            visit.add(n)
            n = self.Sumsquare(n)
            if n == 1:
                return True
        return False
    
    def Sumsquare(self , n)-> int :
        s= 0
        while n:
                m = n%10
                s+= m**2
                n = n//10
        return s