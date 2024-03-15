class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=1
        right=1
        res=[1]*len(nums)
        for i in range(1,len(nums)):
            left*=nums[i-1]
            res[i]=left
        for i in range(len(nums)-2,-1,-1):
            right*=nums[i+1]
            res[i]*=right
        return res
            
            
            
            