class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        ans = []
        count = 0
        for element in s:
            if element == '(':
                stack.append('(')
                count +=1
            elif element == ')' and count >0:
                stack.append(')')
                count-=1
                if count == 0:
                    ans.append("".join(stack))
                    stack = []
            else:
                ans.append("".join(stack))
                stack = []
        print(ans)
        res = ''
        for p in ans:
            temp = p[1:len(p)-1]
            res+= temp
        return res
    
