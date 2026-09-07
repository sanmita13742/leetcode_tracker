class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for x in asteroids:
            while stack and x < 0 and stack[-1] > 0:
                if abs(stack[-1]) < abs(x):
                    stack.pop()
                    continue
                elif stack[-1] == -x:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(x)
        return stack


