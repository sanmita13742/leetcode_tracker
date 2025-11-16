class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n ==2:
            return 2
        jump_ways = [1] * n 
        jump_ways[0] = 1
        jump_ways[1] = 2
        for jump in range(2,n):
            jump_ways[jump] = jump_ways[jump - 1] + jump_ways[jump - 2]
        return jump_ways[n-1]
        