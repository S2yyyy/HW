class Solution:
    def isValid(self, s: str) -> bool:
        pair = {")" : "(", "]": "[", "}": "{"}
        right = ["}", "]", ")"]
        left = ["(", "[", "{"]
        stack = []
        for i in s:
            if len(stack) == 0 and i in right:
                return False
            if i in left:
                stack.append(i)
            else:
                if pair[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return True if len(stack) == 0 else False
