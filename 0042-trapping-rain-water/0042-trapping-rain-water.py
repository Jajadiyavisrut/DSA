class Solution(object):
    def trap(self, height):
        if not height:
            return 0
            
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        ans = 0
        
        while l < r:
            if left_max < right_max:
                l += 1
                
                left_max = max(left_max, height[l])
                ans += left_max - height[l]
            else:
                #change lsta r to r-1 index
                r -= 1
                #check if r and cureent left max which is greater and store if both same then which index is smaller
                right_max = max(right_max, height[r])
                #right max- current r value by positiion
                ans += right_max - height[r]
                
        return ans