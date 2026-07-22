class Solution(object):
    def subarraySum(self, nums, k):
        ans=0
        curr=0
        pre={0:1}
        for  n in nums:
            curr+=n
            diff=curr-k
            ans+=pre.get(diff,0)
            pre[curr]=1+pre.get(curr,0)
        return ans
        