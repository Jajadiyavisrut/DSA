

class Solution(object):
    def canMeasureWater(self, x, y, target):
        if target > x+y:
            return False
        if target==0:
            return True
        
        def get_gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        return target % get_gcd(x,y) == 0
        """
        :type x: int
        :type y: int
        :type target: int
        :rtype: bool
        """
        