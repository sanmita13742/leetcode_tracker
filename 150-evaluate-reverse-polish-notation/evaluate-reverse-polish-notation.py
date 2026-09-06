class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for op in tokens:
            if op == '+':
                n1 = stack.pop()
                n2 = stack.pop()
                ans = n1 + n2
                stack.append(ans)
                #print(f"adding {n2} + {n1} = {ans}")
                #print(f"add: {stack}")
            elif op == '*':
                n1 = stack.pop()
                n2 = stack.pop()
                ans = n1 * n2
                stack.append(ans)
                #print(f"mul {n2} * {n1} = {ans}")
                #print(f"mul: {stack}")
            elif op == '/':
                n1 = stack.pop()
                n2 = stack.pop()
                ans = n2 / n1
                stack.append(int(ans))
                #print(f"dividing {n2} / {n1} = {ans}")
                #print(f"div: {stack,n2,n1}")
            elif op == '-':
                n1 = stack.pop()
                n2 = stack.pop()
                ans = n2 - n1
                stack.append(ans)
                #print(f"sub {n2} - {n1} = {ans}")
                #print(f"sub: {stack,n1,n2}")
            else:
                stack.append(int(op))
        return stack[0]

        