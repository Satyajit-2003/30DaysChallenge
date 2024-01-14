# Use stack to store the nodes.
# If we see two consecutive "#" characters on the top of the stack, we know that the top node can be removed.
# If we reach the end of the string and there is only one node left in the stack, then the tree is valid.

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        p = preorder.split(',')

        for each in p: 
            stack.append(each)
            while len(stack) > 2 and stack[-1] == "#" and stack[-2] == "#": 
                stack.pop() #pop two "#"
                stack.pop()
                if not stack: 
                    return False
                if stack[-1] == "#": 
                    return False
                stack[-1] = "#"
        return len(stack) == 1 and stack.pop() == "#"