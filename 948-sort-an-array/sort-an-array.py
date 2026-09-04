class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left,right):
            res = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] > right[j]:
                    res.append(right[j])
                    j+=1
                else:
                    res.append(left[i])
                    i+=1
            res.extend(left[i:])
            res.extend(right[j:])   
            return res
                
                    

        def mergesort(nums):
            if len(nums) <=1:
                return nums
            m = len(nums)//2
            left = mergesort(nums[:m])
            right = mergesort(nums[m:])
            ans = merge(left,right)
            return ans
            
        return mergesort(nums)