class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s= []
        for c in tokens:

            if c == "*":
                a= s.pop()*s.pop()
                s.append(a)
            elif c== "-":
                a= - (s.pop()) +s.pop()
                s.append(a)
            elif c== "+":
                a = s.pop() + s.pop()
                s.append(a)
            elif c== "/":
                a = pow(s.pop(), -1) * s.pop()
                s.append(int(a))

            else:
                s.append(int(c))
        return s[0]