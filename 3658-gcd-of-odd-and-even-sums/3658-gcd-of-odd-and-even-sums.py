class Solution(object):
    def gcdOfOddEvenSums(self, n):
        even=0
        odd=-1
        for i in range(n):
            even+=2
            odd+=2
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        return n

        