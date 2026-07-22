# class Solution(object):
#     def subarraySum(self, nums, k):
#         ans=0
#         curr=0
#         pre={0:1}
#         for  n in nums:
#             curr+=n
#             diff=curr-k
#             ans+=pre.get(diff,0)
#             pre[curr]=1+pre.get(curr,0)
#         return ans
        
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        sums = 0
        d = dict()
        d[0] = 1
        
        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums-k,0)
            d[sums] = d.get(sums,0) + 1
        
        return(count)