class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cap = {}
        n = len(nums)
        crit = n//3
        res = []

        for x in nums:
            if x in cap:
                cap[x] += 1
            elif len(cap) < 3:
                cap[x] = 1
            else:
                for y in list(cap):
                    cap[y] -= 1
                    if cap[y] == 0:
                        del cap[y]

        for num in cap.keys():
            if nums.count(num) > crit:
                res.append(num)
        return res