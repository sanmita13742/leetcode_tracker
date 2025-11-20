class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        isthere = {}
        for i in range(len(nums)):
            if target - nums[i] in isthere:
                return [i,isthere[target-nums[i]]]
            else:
                isthere[nums[i]] = i 
        