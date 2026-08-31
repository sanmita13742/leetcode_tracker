class Solution:
    def findMin(self, nums: List[int]) -> int:
        def search(left,right):
            if left == right:
                return nums[left]
            mid = (left + right)//2
            if nums[mid+1] < nums[mid]:
                return nums[mid + 1]
            else:
                return min(search(left, mid), search(mid + 1, right))
        return search(0,len(nums)-1)
                                   