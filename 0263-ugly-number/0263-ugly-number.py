class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Ugly numbers must be strictly positive
        if n <= 0:
            return False
            
        # Divide by 2, 3, and 5 as much as possible
        for factor in [2,3,5]:
            while n % factor == 0:
                n //= factor
                
        # If it reduces to 1, it is an ugly number
        return n == 1
