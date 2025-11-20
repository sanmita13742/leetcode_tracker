class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentSum = 0
        maxSum = nums[0]
        for i in range(len(nums)):
            currentSum = max(nums[i],currentSum + nums[i])
            maxSum = max(maxSum,currentSum)
        return maxSum