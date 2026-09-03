class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        f=set()
        if max(nums) < 0:
            return 1
        for num in nums:
            if num in f:
                continue
            f.add(num)
        for i in range(1,max(nums)):
            if i in f:
                continue
            return i
        return max(nums)+1