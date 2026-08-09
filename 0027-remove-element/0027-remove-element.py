class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lptr = 0
        rptr = len(nums)
        while lptr<rptr:
            if nums[lptr] == val:
                rptr-=1
                nums[lptr] = nums[rptr]
            else:
                lptr+=1
        return rptr
        
        
                