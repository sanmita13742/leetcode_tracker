class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique = 1

        for j in range(1, len(nums)):
            if nums[j] != nums[unique - 1]:
                nums[unique] = nums[j]
                unique += 1
        
        return unique