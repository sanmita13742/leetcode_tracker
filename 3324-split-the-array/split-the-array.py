class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        pos = True
        for n in freq:
            if freq[n] >= 3:
                pos = False
        return pos