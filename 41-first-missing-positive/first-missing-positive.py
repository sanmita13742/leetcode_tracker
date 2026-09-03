class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        f=set(nums)
        n = len(nums)
        if max(nums) < 0:
            return 1
        # for num in nums:
        #     if num in f:
        #         continue
        #     f.add(num)
        for i in range(1,n+1):
            if i in f:
                continue
            return i
        return max(nums)+1