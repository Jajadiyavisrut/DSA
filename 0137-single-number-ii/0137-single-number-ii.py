from collections import Counter

class Solution(object):
    def singleNumber(self, nums):
        freq=Counter(nums)
        
        uni=[num for num,count in freq.items() if count==1]
        return uni[0]
        """
        :type nums: List[int]
        :rtype: int
        """
        