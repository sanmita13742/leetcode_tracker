class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        res = [i for i in count.keys() if count[i]>n/3]
        return res