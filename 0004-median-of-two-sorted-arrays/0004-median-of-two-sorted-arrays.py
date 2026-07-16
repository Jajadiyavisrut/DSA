class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the smaller array to minimize binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        total_left = (m + n + 1) // 2
        
        while low <= high:
            # Partition nums1 and calculate corresponding partition for nums2
            partition1 = (low + high) // 2
            partition2 = total_left - partition1
            
            # Identify edge values around the partitions
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if we found the correct partition point
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Odd total length: max of left halves
                if (m + n) % 2 == 1:
                    return float(max(maxLeft1, maxLeft2))
                # Even total length: average of middle boundaries
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            
            # Adjust binary search window
            elif maxLeft1 > minRight2:
                high = partition1 - 1
            else:
                low = partition1 + 1

        ##############################################
        # code by me
        # num=nums1+nums2

        # num.sort()
        # n=len(num)

        # if n%2==0:
        #     ans=float((num[(n//2)-1]+num[(n//2)])/2.0)
        # elif n%2==1:
        #     ans=float(num[n//2])
        # return ans
        #####################################
        # num1=nums1.extend(nums2)
        # if (len(num1)%2)==0:
        #     ans=float(num1[int(len(num1)/2)]+num1[int(len(num1)/2)+1]
        # elif (len(num1)%2)==1:
        #     ans=float(num1[int(len(num1))+1])
        # return len(num1)
        