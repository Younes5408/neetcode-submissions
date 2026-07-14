class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        close={")":"(","]":"[","}":"{"}
        for k in s :
            if k in close:
                if a and a[-1]== close[k]:
                    a.pop()
                else:
                    return False
            else:
                a.append(k)
        return True if not a else False