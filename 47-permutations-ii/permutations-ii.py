class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm = []
        count = Counter(nums)
        res = []
        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for n in count:
                if count[n] > 0:
                    count[n] -=1
                    perm.append(n)
                    dfs()
                    perm.pop()
                    count[n]+=1
        dfs()
        return res


        