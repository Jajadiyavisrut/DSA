class Solution(object):
    def sortArrayByParity(self, nums):
        # nums=nums.sorted()
        even=[]
        odd=[]
        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        even.extend(odd)
        return even
        