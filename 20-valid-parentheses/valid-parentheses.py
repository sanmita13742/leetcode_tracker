class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            '[':']',
            '{':'}',
            '(':')'
        }
        for bracket in s:
            if bracket in "[{(":
                stack.append(bracket)
            elif bracket in ')}]' and stack and  pair[stack[-1]] == bracket :
                stack.pop()
            else:
                return False
        if stack:
            return False
        else:
            return True