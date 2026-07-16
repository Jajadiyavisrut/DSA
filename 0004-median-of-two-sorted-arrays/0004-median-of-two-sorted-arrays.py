class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        num=nums1+nums2

        num.sort()
        n=len(num)

        if n%2==0:
            ans=float((num[(n//2)-1]+num[(n//2)])/2.0)
        elif n%2==1:
            ans=float(num[n//2])
        return ans
        
        # num1=nums1.extend(nums2)
        # if (len(num1)%2)==0:
        #     ans=float(num1[int(len(num1)/2)]+num1[int(len(num1)/2)+1]
        # elif (len(num1)%2)==1:
        #     ans=float(num1[int(len(num1))+1])
        # return len(num1)
        