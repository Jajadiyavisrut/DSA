class Solution(object):
    def twoSum(self, nums, target):
        dic={}
        for i,n in enumerate(nums):
            dif=target-n
            if dif in dic:
                return [dic[dif],i]
            dic[n]=i
        return 