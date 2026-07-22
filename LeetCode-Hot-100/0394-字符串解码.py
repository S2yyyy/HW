class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        char_stack = []
        i = 0
        while i < len(s):
            char = s[i]
            if '0' <= char <= '9':
                num = 0
                while s[i] != '[':
                    num = num * 10 + int(s[i])
                    i += 1
                i -= 1
                num_stack.append(num)
            elif 'a' <= char <= 'z' or char == '[':
                char_stack.append(char)
            elif char == ']':
                sub = ''
                while char_stack[-1] != '[':
                    sub = char_stack.pop() + sub
                char_stack.pop()
                sub *= num_stack.pop()
                char_stack.append(sub)
            i += 1
        return "".join(char_stack)

