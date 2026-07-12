class Solution(object):
    def twoSum(self, numbers, target):
      # solution 1
        # dic={}
        # for i,n in enumerate(numbers):
        #     dif=target-n
        #     if dif in dic:
        #         return [dic[dif]+1,i+1]
        #     dic[n]=i     

        # solution 2 using two pointer
        l,r=0,len(numbers)-1
        while l<r:
            ans=numbers[l]+numbers[r]
            if ans>target:
                r=r-1
            elif ans<target:
                l=l+1 
            else:
                return [l+1,r+1]