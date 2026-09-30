class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort()
        nums=nums[::-1]
        return nums[k-1]
        