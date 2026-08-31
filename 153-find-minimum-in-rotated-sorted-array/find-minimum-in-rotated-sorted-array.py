class Solution:
    def findMin(self, nums: List[int]) -> int:
        def search(l, r):
            if l == r:
                return nums[l]

            m = (l + r) // 2

            if nums[m] > nums[r]:
                return search(m + 1, r)
            return search(l, m)

        return search(0, len(nums) - 1)