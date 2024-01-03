# Use a stack
# When I: push the number to stack and pop all the numbers in the stack
# When D: push the number to stack
# In the end, push the last number to stack and pop all the numbers in the stack

class Solution:
    def printMinNumberForPattern(ob,S):
        # code here 
        stack = []
        res = ''
        i = 1
        for ch in S:
            if ch == 'I':
                stack.append(str(i))
                while stack:
                    res += stack.pop()
            if ch == 'D':
                stack.append(str(i))
            i += 1
        stack.append(str(i))
        while stack:
            res += stack.pop()
        return res