class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ptr1 = 0
        ptr2 = 1
        twice = 0
        nums.sort()
        while ptr2 < len(nums) :
            if nums[ptr2] == nums[ptr1]:
                ptr2+=1
                if ptr2 - ptr1 ==2:
                    
                    return True
                
            else:
                ptr1+=1
                ptr2+=1
        print(ptr2 - ptr1)
        return False

                
