class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        m = len(pattern)
        l, r = 0, m
        res = 0
        temp = True
        i = 0

        while r < len(nums):
            k = l - i

            if pattern[k] == 1 and nums[l+1] > nums[l]:
                pass
            elif pattern[k] == 0 and nums[l+1] == nums[l]:
                pass
            elif pattern[k] == -1 and nums[l+1] < nums[l]:
                pass
            else:
                temp = False

            if l == r - 1:
                if temp:
                    res += 1

                i += 1
                l = i
                r = i + m
                temp = True
            else:
                l += 1

        return res