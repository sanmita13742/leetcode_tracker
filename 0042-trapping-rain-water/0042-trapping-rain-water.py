class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0]*(n+1)
        maxRight = [0]*(n+1)
        
        count = 0
        for i in range(n):
            maxLeft[i] = max(maxLeft[i-1],height[i])
       
        for i in range(len(height)-1,-1,-1):
            maxRight[i] = max(maxRight[i+1],height[i])
        maxLeft = maxLeft[:-1]
        maxRight = maxRight[:-1]
        # print(maxLeft)
        # print(maxRight)
        for i in range(n):
            res = min(maxRight[i],maxLeft[i])
            if res  - height[i]>0:
                count+= res - height[i]
        return count