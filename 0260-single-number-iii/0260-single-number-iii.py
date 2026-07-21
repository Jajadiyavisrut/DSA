class Solution(object):
    def singleNumber(self, nums):
        if len(nums)== 2:
            return nums
        
        dic={}
        # s,e=0,len(nums)-1
        # while s<e:
        #     dic[nums[s]]=+1
        #     dic[nums[e]]=+1
        #     s+=1
        #     e+=1
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        return [k for k,v in dic.items() if v==1]
        # return dic