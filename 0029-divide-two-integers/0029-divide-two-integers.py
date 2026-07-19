class Solution(object):
    def divide(self, dividend, divisor):
        # ans=int(dividend//divisor)
        # if ans>=0:
        #     return ans
        # elif ans<0:
        #     return ans+1 
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
            
        # 2. Use float division inside int() to truncate properly toward zero
        ans = int(float(dividend) / divisor)
        
        return ans