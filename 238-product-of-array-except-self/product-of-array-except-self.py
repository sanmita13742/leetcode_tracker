class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        prefix = [1] * (n)
        prefix[0] = nums[0]
        suffix = [1] * (n)
        suffix[-1] = nums[-1]
        last = n-2
        for i in range(1,n):
            prefix[i] *= prefix[i-1]* nums[i]
            suffix[last] = suffix[last+1] * nums[last]
            last-=1
        nums[0] = suffix[1]
        nums[-1] = prefix[-2]
        for i in range(1,n-1):
            nums[i] = prefix[i-1] * suffix[i+1]
        return nums
