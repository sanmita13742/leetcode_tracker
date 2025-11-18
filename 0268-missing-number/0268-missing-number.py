class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum_Full = 0
        for i in range(n+1): sum_Full +=i
        return sum_Full - sum(nums)

        
        