class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        ans = 0
        for num in numset:
            if num -1 not in numset:
                i = num
                temp = 1
                while i+1 in numset :
                    i+=1
                    temp+=1
                ans = max(ans,temp)
                
        return ans 


