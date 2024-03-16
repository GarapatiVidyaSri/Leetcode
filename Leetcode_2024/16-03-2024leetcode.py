class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        h={}
        max_length=0
        sum_val=0
        for i in range(len(nums)):
            sum_val+=1 if nums[i]==1 else -1   
            if sum_val==0:
                max_length=i+1
            elif sum_val in h:
                max_length=max(max_length,i-h[sum_val])
            else:
                h[sum_val]=i
        return max_length