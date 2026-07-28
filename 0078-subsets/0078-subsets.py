class Solution(object):
    def subsets(self, nums):
        arr=[]
        arr.append([])
        for num in nums:
            arr+=[curr+[num] for curr in arr]
        return arr