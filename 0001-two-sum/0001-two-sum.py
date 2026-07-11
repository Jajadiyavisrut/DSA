class Solution(object):
    def twoSum(self, nums, target):
        ans=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    pass
                else:
                    if nums[i]+nums[j]==target:
                        ans.extend([i,j])
                        return ans
        return ans
        