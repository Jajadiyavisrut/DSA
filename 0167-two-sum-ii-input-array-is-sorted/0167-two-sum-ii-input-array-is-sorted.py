class Solution(object):
    def twoSum(self, numbers, target):
        dic={}
        for i,n in enumerate(numbers):
            dif=target-n
            if dif in dic:
                return [dic[dif]+1,i+1]
            dic[n]=i        