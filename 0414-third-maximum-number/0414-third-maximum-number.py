class Solution(object):
    def thirdMax(self, nums):
        nums=list(set(nums))
        nums=sorted(nums,reverse=True)
        ans=0
        if len(nums)<3:
            ans=max(nums)
        else:
            ans=nums[2]
        return ans